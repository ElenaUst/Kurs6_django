from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import index, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView, \
    MailingListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MessageDetailView, MessageListView, \
    ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView, ClientListView, LogsListView

app_name = MailingConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/<int:pk>/', cache_page(60)(MailingDetailView.as_view()), name='mailing'),
    path('mailing/mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/message_create/', MessageCreateView.as_view(), name='message_create'),
    path('mailing/<int:pk>/message_update/', MessageUpdateView.as_view(), name='message_update'),
    path('mailing/<int:pk>/message_delete/', MessageDeleteView.as_view(), name='message_delete'),
    path('mailing/message/<int:pk>/', MessageDetailView.as_view(), name='message'),
    path('mailing/message_list/', MessageListView.as_view(), name='message_list'),
    path('mailing/client_create/', ClientCreateView.as_view(), name='client_create'),
    path('mailing/<int:pk>/client_update/', ClientUpdateView.as_view(), name='client_update'),
    path('mailing/<int:pk>/client_delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('mailing/client/<int:pk>/', ClientDetailView.as_view(), name='client'),
    path('mailing/client_list/', ClientListView.as_view(), name='client_list'),
    path('mailing/logs/', LogsListView.as_view(), name='logs'),
]