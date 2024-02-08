from datetime import datetime, timezone, timedelta
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F


from mailing.models import Mailing, Logs


def start_mailing():
    """Функция запуска рассылки"""
    now = datetime.now(timezone.utc)
    mailing_list = Mailing.objects.filter(last_time__lte=now)
    for mailing in mailing_list:
        title = mailing.template.title

        message = mailing.template.message
        try:
            send_mail(
                subject=title,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.mail_to.all()],
                fail_silently=False,

            )
            if mailing.interval == 'onetime':
                mailing.last_time = None
                mailing.mailing_status = 'completed'
            elif mailing.interval == '1':
                mailing.last_time = F('last_time') + timedelta(days=1)
                mailing.mailing_status = 'launched'
            elif mailing.interval == '7':
                mailing.last_time = F('last_time') + timedelta(days=7)
                mailing.mailing_status = 'launched'
            elif mailing.interval == '30':
                mailing.last_time = F('last_time') + timedelta(days=30)
                mailing.mailing_status = 'launched'
            mailing.save()
            try_status = 'good'
            server_response = 'успешно'

        except smtplib.SMTPException as error:
            try_status = 'bad'
            server_response = str(error)

        finally:
            Logs.objects.create(mailing=mailing, try_status=try_status, server_response=server_response, last_try_datetime=now)





