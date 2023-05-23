from django.urls import path
from .views import *

urlpatterns = [
    path('contacts/', ContactView.as_view(), name='contact'),
    path('contacts/<int:id>/', ContactDetailView.as_view(), name='contact_detail'),
    path('contacts/create/', ContactDetailView.as_view(), name='contact_detail'),
    path('socials/', SocialMediaLinksView.as_view(), name='social_media'),
    path('socials/<int:id>/', SocialMediaLinksDetailView.as_view(), name='social_media_detail'),
    path('socials/create/', SocialMediaLinksDetailView.as_view(), name='social_media_detail'),
]
