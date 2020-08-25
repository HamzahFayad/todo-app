from django.contrib.auth.models import User
from django import forms


class CreateUserForm(forms.ModelForm):
    profile_picture = forms.ImageField()
    bio = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'bio')
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': None,
        }