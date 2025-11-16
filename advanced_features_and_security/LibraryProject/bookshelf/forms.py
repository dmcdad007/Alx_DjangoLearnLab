# bookshelf/forms.py
from django import forms
from .models import BookReview
from .forms import ExampleForm

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not (1 <= rating <= 5):
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

    def clean_comment(self):
        comment = self.cleaned_data['comment']
        if len(comment) > 1000:
            raise forms.ValidationError("Comment is too long.")

        return comment.strip()
        ExampleForm

