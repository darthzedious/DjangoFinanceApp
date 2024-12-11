from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from financeDjango.accounts.models import Profile
from financeDjango.mixins import PlaceholderMixin

UserModel = get_user_model()

class RegisterForm(PlaceholderMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username','email']


class AppUserChangeForm(PlaceholderMixin, UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'

class ProfileEditForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.attrs.update({
             'placeholder': 'Profile picture URL'
        })


class LoginForm(PlaceholderMixin, AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username or email'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )