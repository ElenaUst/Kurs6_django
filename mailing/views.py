from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from blog.models import Blog
from mailing.forms import MailingForm, MessageForm, ClientForm, ManagerMailingForm
from mailing.models import Mailing, Message, Client, Logs


def index(request):
    count_mailing = Mailing.objects.all()
    active_mailing = Mailing.objects.filter(mailing_status='launched')
    count_unique_client = Client.objects.values('email').distinct()
    articles = Blog.objects.order_by('?')[:3]
    context = {'count_mailing': count_mailing, 'active_mailing': active_mailing, 'count_unique_client': count_unique_client, 'articles': articles}

    return render(request, 'users/index.html', context)


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания новой рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')
    # login_url = reverse_lazy('mailing:access_denied')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для изменения новой рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return MailingForm
        elif self.request.user.has_perm('mailing.set_deactivate'):
            return ManagerMailingForm
        else:
            raise Http404('Вы не имеете права на редактирование рассылок')


class MailingListView(ListView):
    """Класс для просмотра списка рассылок"""
    model = Mailing


class MailingDetailView(DetailView):
    """Класс для просмотра отдельной рассылки"""
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:index')


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания сообщения для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для изменения сообщения для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageListView(ListView):
    """Класс для просмотра списка сообщений для рассылок"""
    model = Message


class MessageDetailView(DetailView):
    """Класс для просмотра отдельного сообщения для рассылки"""
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления сообщения для рассылки"""
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания новой рассылки"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для изменения сообщения для рассылки"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientListView(ListView):
    """Класс для просмотра списка сообщений для рассылок"""
    model = Client


class ClientDetailView(DetailView):
    """Класс для просмотра отдельного сообщения для рассылки"""
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления сообщения для рассылки"""
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class LogCreate(CreateView):
    model = Logs

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class LogsListView(LoginRequiredMixin, ListView):
    """Вывод списка логов рассылок пользователя"""
    model = Logs

    # def get_queryset(self):
    #     """Метод для вывода логов только текущего пользователя"""
    #     return super().get_queryset().filter(user=self.request.user)




