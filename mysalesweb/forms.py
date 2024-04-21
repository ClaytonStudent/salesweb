
from django import forms
from .Entities import product

class ProductAddForm(forms.ModelForm):
	name = forms.CharField(max_length=200)
	location = forms.CharField(max_length=255, required=False)
	quantity = forms.IntegerField()
	class Meta:
		model = product.Product
		fields =  '__all__' # ['name','location']#