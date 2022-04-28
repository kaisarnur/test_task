from django import forms
from webapp.models import Shop, Good


class ShopForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Shop


class GoodForm(forms.ModelForm):
    class Meta:
        exclude = ["shop"]
        model = Good
