from django import forms
from .models import India


class IndiaForm(forms.ModelForm):
    class Meta:
        model = India
        fields = "__all__"

        widgets = {
            "state": forms.TextInput(attrs={"class": "form-control"}),
            "capital": forms.TextInput(attrs={"class": "form-control"}),
            "population": forms.NumberInput(),
            "famous_food": forms.TextInput(attrs={"class": "form-control"}),
            "popular_temples": forms.TextInput(attrs={"class": "form-control"}),
            "no_of_taluka": forms.NumberInput()
        }
