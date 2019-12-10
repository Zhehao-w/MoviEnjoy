from django import forms
from review.models import Review
from django.contrib.auth.models import User




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('movie', 'author', 'title', 'content','created_date')

