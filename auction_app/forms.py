from django import forms

class BidForm(forms.Form):
    bid_amount = forms.FloatField(min_value=0)
