# Generated by Django 4.2 on 2024-02-08 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_alter_mailing_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('set_deactivate', 'Can deactivate mailing'), ('view_all_mailings', 'Can view all mailing')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
