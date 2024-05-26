from django import forms


class SelOffEls(forms.Form):
    select_field = forms.ChoiceField(label=False)


class SelTemperature(forms.Form):
    temperature_field = forms.CharField(max_length=10)
