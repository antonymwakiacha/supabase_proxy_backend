from django.urls import path
from .views import get_words, get_idioms

urlpatterns = [
    path('words/', get_words, name='get_words'),
    path('idioms/', get_idioms, name='get_idioms'),
]
