from django import forms
from .models import Content


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ['blog_id', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }