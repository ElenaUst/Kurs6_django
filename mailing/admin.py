from django.contrib import admin

from mailing.models import Mailing, Logs


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'try_status')
