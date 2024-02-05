from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    """Класс для формы регистрации пользователя"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class UserForm(UserChangeForm):
    """Класс для формы профиля пользователя"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


# class ManagerUserForm(UserForm):
#     """Класс формы пользователя для менеджера"""
#     class Meta:
#         model = User
#         fields = ('is_active',)