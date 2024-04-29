from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class CreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ('email',)

class CreationForm(UserCreationForm):
    ...
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
        }