from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileUpdateView, RegisterView, UserListView, toggle_activity_user

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('user_list/', UserListView.as_view(), name='users-list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('toggle_user/<int:pk>/', toggle_activity_user, name='toggle-activity-user')
]
