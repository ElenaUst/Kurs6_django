from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс для создания модели пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта пользователя')

    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='комментарий')
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=250, verbose_name='токен пользователя', blank=True,
                                                null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        permissions = [
            (
             'set_user_deactivate',
             'Can deactivate user'
            ),
            ('view_all_users',
             'просмотр всех пользователей'
             ),
        ]


