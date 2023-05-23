from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/create/', ProfileDetailView.as_view(), name='profile_detail'),
]

