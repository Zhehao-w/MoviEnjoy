from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

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