# Generated by Django 4.2 on 2024-02-03 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_user_deactivate', 'Can deactivate user')]},
        ),
    ]