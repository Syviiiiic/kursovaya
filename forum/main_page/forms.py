from django import forms
from .models import Comment, Subject


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Enter your comment'
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('title', 'category', 'body',)
        labels = {
            'title': 'Title',
            'category': 'Category',
            'body': 'Body',
        }

