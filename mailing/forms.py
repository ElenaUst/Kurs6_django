from django import forms

from mailing.models import Mailing, Message, Client


class MailingForm(forms.ModelForm):
    """Класс для формы рассылки"""
    class Meta:
        model = Mailing
        exclude = ('user', 'last_date',)


class ManagerMailingForm(MailingForm):
    """Класс для формы менеджера"""
    class Meta:
        model = Mailing
        fields = ('mailing_status',)


class MessageForm(forms.ModelForm):
    """Класс для формы сообщения для рассылки"""
    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(forms.ModelForm):
    """Класс для формы клиента для рассылки"""
    class Meta:
        model = Client
        fields = '__all__'

