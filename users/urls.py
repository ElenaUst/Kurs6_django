from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import RegisterView, activate, VerificationFailedView, UserUpdateView, UserListView, toggle_active

app_name = UsersConfig.name


urlpatterns = [

    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='users'),
    path('toggle_active/<int:pk>/', toggle_active, name='toggle_active'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    path('verification_failed/', VerificationFailedView.as_view(), name='verification_failed'),

]