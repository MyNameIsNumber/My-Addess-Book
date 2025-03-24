from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ["name", "email", "phone", "address_first_line", "address_second_line", "town", "postcode",]