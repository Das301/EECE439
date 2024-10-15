from django import forms


class CreateBookForm(forms.Form):
    title = forms.CharField(label='title')
    author = forms.CharField(label='author')