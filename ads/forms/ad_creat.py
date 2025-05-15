from django import forms
from django.core import validators
from django.utils.translation import gettext_lazy as _


class adCreatForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter the title"}),
    )
    content = forms.CharField(widget=forms.Textarea)
    image_field = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        required=False,
        help_text="Your file must be one from these: 'jpg', 'jpeg', 'png'",
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png"]
            ),
        ],
    )

    # def clean_image_field(self):
    #     files = self.image_field
    #     pass
    # if (len(files) > 5):
    #     raise forms.ValidationError(_("Maximum quantity of files is 5!"))
