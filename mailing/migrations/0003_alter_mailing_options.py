# Generated by Django 4.2 on 2024-02-03 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_client_mailing_logs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('set_deactivate', 'Can deactivate mailing')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
