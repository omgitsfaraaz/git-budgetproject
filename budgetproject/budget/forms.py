from django import forms

class ExpenseForm(forms.Form):
	title = forms.Charfield()
	amount = forms.IntegerField()
	category = forms.Charfield()