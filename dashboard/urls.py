from django.urls import path
from .views import *


urlpatterns = [
    path('new_review', new_review, name='new_review'),
    path('list_reviews', list_reviews, name='list_reviews'),
    path('new_review_v2', NewReview.as_view(), name='new_review_v2'), 
    path('list_reviews_v2', ListReviews.as_view(), name='list_reviews_v2')
]
