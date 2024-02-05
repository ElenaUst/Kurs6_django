# Generated by Django 5.0 on 2024-01-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='клиент сервиса')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='почта')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
    ]
