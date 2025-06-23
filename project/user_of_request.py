from asgiref.sync import sync_to_async
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UsageUsers:
    """
    This class gets and returns the user from db or errors if user is not founded.
    :return: Method `user = self.user` returns the user from db or error.
    Example:
    ```python
    from project.user_of_requesst import UsageUsers
    users_users = UsageUsers(request)
    user = users_users.user
    ```
    """

    def __init__(self, request):
        """
        This is constructor.
        :param request: request object
        """
        self.request = request
        self.request_user = request.user

    def __get_user_db(self):
        """
        This method gets and returns the user from db or errors if user is not founded.
        :return: user object or error
        """
        cl = __class__.__name__
        try:
            """SEARCH USER IN DB"""
            request_user_id: int = self.request_user.id

            user = User.objects.filter(id=request_user_id).first()
            if not user:
                """USER IS NOT FOUND"""
                raise ValidationError(
                    "%s: user is not founded." % cl.__get_user_db.__name__
                )
            return user
        except Exception as error:
            cl = __class__.__name__
            raise ValidationError(
                "%s: user is invalid. %s" % (cl.__get_user_db.__name__, error)
            )

    @property
    def user(self):
        """
        This method gets and returns the user from db or errors if user is not founded.
        :return: user object or error
        """
        cl = __class__.__name__
        try:
            user = self.__get_user_db()
            return user
        except Exception as error:
            raise ValidationError("%s: %s" % (cl.__get_user_db.__name__, error))
