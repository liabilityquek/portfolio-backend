from django.urls import path, include
# from .views import RegisterView, LoginView, get_csrf, ResetPasswordView
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', Auth0UserView, name="login"),
]   