from django.db import models
from django.utils import timezone

from users.models import User


class Client(models.Model):
    """Модель клиентов - получателей рассылки"""
    email = models.EmailField(verbose_name='почта клиента для рассылки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='пользователь сервиса')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        unique_together = ('user', 'email',)


class Message(models.Model):
    """Модель сообщения для рассылки"""
    title = models.CharField(max_length=150, verbose_name='тема сообщения')
    message = models.TextField(max_length=500, verbose_name='текст сообщения')

    def __str__(self):
        return f'{self.title} {self.message}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    """Модель рассылки"""
    INTERVAL_CHOICES = [
        ('onetime', 'один раз'),
        ('1', 'ежедневно'),
        ('7', 'еженедельно'),
        ('30', 'ежемесячно'),
    ]
    STATUS_CHOICES = [
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена'),
    ]

    name = models.CharField(max_length=150, verbose_name='название рассылки')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='дата и время создания рассылки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='пользователь сервиса')
    last_time = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name='время отправки рассылки')

    mail_to = models.ManyToManyField(Client, verbose_name='клиенты для рассылки')
    interval = models.CharField(max_length=50, choices=INTERVAL_CHOICES, default='', verbose_name='периодичность рассылки')
    mailing_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created', verbose_name='статус рассылки')
    template = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, verbose_name='сообщение для рассылки')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            (
                'set_deactivate',
                'Can deactivate mailing'
            ),
        ]


class Logs(models.Model):
    """Модель логов рассылки"""
    TRY_STATUS_CHOICES = [
        ('good', 'успешно'),
        ('bad', 'неуспешно'),
    ]
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, null=True, verbose_name='рассылка')
    last_try_datetime = models.DateTimeField(blank=True, null=True, verbose_name='дата и время последней попытки')
    try_status = models.CharField(max_length=50, choices=TRY_STATUS_CHOICES, default='', blank=True, null=True, verbose_name='статус попытки')
    server_response = models.CharField(max_length=250, blank=True, null=True, verbose_name='ответ сервера')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='пользователь сервиса')

    def __str__(self):
        return f'{self.mailing}: {self.last_try_datetime} {self.try_status} {self.server_response} {self.user}'

    class Meta:
        verbose_name = 'попытка отправки'
        verbose_name_plural = 'попытки отправки'


