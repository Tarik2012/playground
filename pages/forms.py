from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page  # Nota: usa '=' en vez de ':'
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content', 'rows': 5}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'orden'}),
        }

        labels = {
            'title':'', 'order':''
        }