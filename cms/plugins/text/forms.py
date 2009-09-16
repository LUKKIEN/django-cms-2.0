from django.forms.models import ModelForm
from cms.plugins.text.models import Text
from django import forms


class TextForm(ModelForm):
    body_storage = forms.CharField()
    
    class Meta:
        model = Text
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
        