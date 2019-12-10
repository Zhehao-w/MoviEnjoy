from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

from review.forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class ReviewListView(ListView):

    model = models.Review


class ReviewDetailView(DetailView):
    context_object_name = 'review_details'
    model = models.Review
    template_name = 'review/review_detail.html'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    fields = ("movie","title","content","created_date")
    model = models.Review


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("title","content")
    model = models.Review


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Review
    success_url = reverse_lazy("review:list")

@login_required
def create_review(request):

    created = False

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():

            review = review_form.save()
            review.save()

            created = True

        else:
            print(review_form.errors)

    else:

        review_form = ReviewForm()


    return render(request, 'review/create_review.html', {'review_form': review_form,'created': created})