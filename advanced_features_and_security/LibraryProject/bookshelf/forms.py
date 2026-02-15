from .models import Book
from django import forms
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

