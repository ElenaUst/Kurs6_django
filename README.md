Для запуска проекта необходимо в файле settings.py внести данные для подключения к БД по шаблону:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Django_project',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
        'PASSWORD': 'user_password'

    }
}

Переименуйте env_example в .env и заполните переменные окружения своими значениями