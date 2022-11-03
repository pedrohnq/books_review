from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *


# Create your views here.

def new_review(request):
    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Salvo!')
    else:
        form = BookReviewForm()
    return render(request, 'book_review_form.html', {'form': form})


def list_reviews(request):
    reviews = BookReview.objects.all().order_by('title')
    return render(request, 'book_review_list.html', {'reviews': reviews})