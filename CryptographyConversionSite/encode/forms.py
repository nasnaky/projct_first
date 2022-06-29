from django import forms

from .models import ChangeEncode


class ChangeEncodeForm(forms.ModelForm):
    class Meta:
        model = ChangeEncode
        fields = ['origen']
        widgets = {
            'origen': forms.Textarea(attrs={'class': 'orig'}),
        }
