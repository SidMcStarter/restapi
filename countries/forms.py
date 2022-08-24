from django import forms
from countries.models import Country

class CreateCountryForm(forms.ModelForm):
    # currency_name = forms.CharField(max_length=100,label="Currency Name",required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    # currency_symbol = forms.CharField(max_length=100,label="Currency Symbol",required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Country
        exclude = ["user"]
        labels = {
            "currencies":"Currencies(Name and Symbol)"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "capital": forms.TextInput(attrs={"class":"form-control"}),
            "region": forms.TextInput(attrs={"class":"form-control"}),
            "subregion": forms.TextInput(attrs={"class":"form-control"}),
            "population": forms.TextInput(attrs={"class":"form-control"}),
            "image": forms.URLInput(attrs={"class":"form-control"}),
            "languages": forms.Textarea(attrs={"class":"form-control","rows":"3"}),
            "currencies": forms.Textarea(attrs={"class":"form-control","rows":"3"})
        }
        help_texts = {
            "languages": 'Input example: ["English","French"]',
            "currencies": 'Input example: [{"name":"USD","symbol":"$"}]'
        }