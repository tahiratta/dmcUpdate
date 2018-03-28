from django import forms

class contactForm(forms.Form):
	name = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
	email = forms.EmailField(required=True)
	subject = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
	message = forms.CharField(required=True, widget=forms.Textarea)

class careersForm(forms.Form):
	name = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
	email = forms.EmailField(required=True)
	subject = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
	file = forms.FileField(label='Your Resume', widget = forms.FileInput, required = True)
	message = forms.CharField(required=True, widget=forms.Textarea)

	