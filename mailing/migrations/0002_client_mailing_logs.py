# Generated by Django 4.2 on 2024-02-03 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='почта клиента для рассылки')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь сервиса')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'unique_together': {('user', 'email')},
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название рассылки')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата и время создания рассылки')),
                ('last_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='время отправки рассылки')),
                ('interval', models.CharField(choices=[('onetime', 'один раз'), ('1', 'ежедневно'), ('7', 'еженедельно'), ('30', 'ежемесячно')], default='', max_length=50, verbose_name='периодичность рассылки')),
                ('mailing_status', models.CharField(choices=[('completed', 'завершена'), ('created', 'создана'), ('launched', 'запущена')], default='created', max_length=50, verbose_name='статус рассылки')),
                ('mail_to', models.ManyToManyField(to='mailing.client', verbose_name='клиенты для рассылки')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='сообщение для рассылки')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь сервиса')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try_datetime', models.DateTimeField(blank=True, null=True, verbose_name='дата и время последней попытки')),
                ('try_status', models.CharField(blank=True, choices=[('good', 'успешно'), ('bad', 'неуспешно')], default='', max_length=50, null=True, verbose_name='статус попытки')),
                ('server_response', models.CharField(blank=True, max_length=250, null=True, verbose_name='ответ сервера')),
                ('mailing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.mailing', verbose_name='рассылка')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь сервиса')),
            ],
            options={
                'verbose_name': 'попытка отправки',
                'verbose_name_plural': 'попытки отправки',
            },
        ),
    ]
