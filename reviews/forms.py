from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea(attrs={
        'class': "materialize-textarea",
        'placeholder': "Add a New Review",
    }), label='New Review')

    rate_choice = [('', 'Rate It'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), ]
    rating = forms.IntegerField(widget=forms.Select(choices=rate_choice),
                                label='')

    class Meta:
        model = Review
        fields = ['review_text', 'rating']
