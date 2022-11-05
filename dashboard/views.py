from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView

# Create your views here.

def new_review(request):
    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_reviews')
    else:
        form = BookReviewForm()
    return render(request, 'book_review_form.html', {'form': form})


class NewReview(CreateView):
    model = BookReview
    form_class =  BookReviewForm
    template_name = 'book_review_form.html'
    success_url = 'list_reviews'


def list_reviews(request):
    object_list = BookReview.objects.all().order_by('title')
    return render(request, 'book_review_list.html', {'object_list': object_list})


class ListReviews(ListView):
    queryset = BookReview.objects.all().order_by('title')
    template_name = 'book_review_list.html'
