from django.urls import path
from .views import *

urlpatterns = [
    path('socials/', SocialMediaLinksView.as_view(), name='social_media'),
    path('socials/<int:id>/', SocialMediaLinksDetailView.as_view(), name='social_media_detail'),
    path('socials/create/', SocialMediaLinksDetailView.as_view(), name='social_media_detail'),
]
