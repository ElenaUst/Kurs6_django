from django.core.management import BaseCommand

from mailing.services import start_mailing


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start_mailing()



