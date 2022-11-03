from django.urls import path
from .views import *


urlpatterns = [
    path('new_review', new_review, name='new_review'),
    path('list_reviews', list_reviews, name='list_reviews'),
]
