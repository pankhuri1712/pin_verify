from django import forms



class create_pin(forms.Form):
    mobile_number= forms.CharField(max_length=10)

    name= forms.CharField(max_length=100)

class verify_pin(forms.Form):
    PIN = forms.CharField(max_length=5)
