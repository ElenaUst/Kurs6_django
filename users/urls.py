from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, activate, VerificationFailedView, UserListView, UserDetailView

app_name = UsersConfig.name


urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/detail', UserDetailView.as_view(), name='profile'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    path('verification_failed/', VerificationFailedView.as_view(), name='verification_failed'),

]