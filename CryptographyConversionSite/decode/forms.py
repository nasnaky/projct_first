from django import forms

from .models import ChangeDecode


class ChangeDecodeForm(forms.ModelForm):
    class Meta:
        model = ChangeDecode
        fields = ['origen']
        widgets = {
            'origen': forms.Textarea(attrs={'class': 'orig'}),
        }
