"""
project/groups.py
"""

"""
```html
{% if user.groups.filter(name='Ad Author').exists %}
    <p>Это автор объявлений</p>
{% endif %}
```
and
```python
if request.user.groups.filter(name='Ad Author').exists():
    print("Пользователь в группе Ad Authors")
else:
    print("Пользователь НЕ в группе")
```
or
```python
user.groups.filter(name='Ad Author').exists()

```
"""

# from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from project.user_of_request import UsageUsers


class Groups(UsageUsers):
    """
    Group has dependence from 'UsageUsers'.
    The class provided a functionality for adding and checking user to a group \
    through the method 'user_to_groups'.

    You can to check user in a grop. It is method 'check_user_in_group'.
    And, getting user of db. It's the method 'user'.
    Or, getting user of request, It's through the variable '`request_user`'.  from request. \
    """

    def __group(self, group_name: str):
        cl = __class__.__name__

        try:
            group = Group.objects.filter(name=group_name).first()
            return group
        except Exception as error:
            raise ValidationError(
                "%s: error. Group-  '%s': %s" % (cl, group_name, error)
            )

    def user_to_groups(self, group_name: str) -> bool:
        """
        This method provided functionally for adding a user to the group 'group_name'.
        :param group_name: str. It's group's name where we want to add the user.
        :return bool. If all is OK. then returns 'True' else error.
        """
        cl = __class__.__name__
        usage_user = self.user
        try:
            group = self.__group(group_name)
            usage_user.groups.add(group)
            usage_user.save()
            return True
        except Exception as error:
            raise ValidationError(
                "%s: error. User not added to the group - '%s': %s"
                % (cl, group_name, error)
            )

    def check_user_in_group(self, group_name: str) -> bool:
        """
        This method provided functionally for checking if the user is in the group 'group_name'.
        :param group_name: str. It's group's name.
        :return bool: If user was found to the group, return 'True' else 'False'.
        """
        cl = __class__.__name__
        usage_user = self.user
        try:
            group = self.__group(group_name)
            if group in usage_user.groups.all():
                return True
            else:
                return False
        except Exception as error:
            raise ValidationError(
                "%s: error. Check user in the group - '%s': %s"
                % (cl, group_name, error)
            )
