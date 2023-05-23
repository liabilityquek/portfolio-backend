from django.urls import path
from .views import RegisterView, LoginView, get_csrf, ResetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('login/', LoginView.as_view(), name="login"),
    path('reset-password', ResetPasswordView.as_view(), name='password_reset'), 
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('get-csrf/', get_csrf, name='get_csrf'),
]
      