from django import forms
from dmc.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'name', 'email', 'subject', 'document', 'message' )

class contactForm(forms.Form):
	name = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
	email = forms.EmailField(required=True)
	subject = forms.CharField(required=True, max_length=100, help_text='100 characters max.')
	message = forms.CharField(required=True, widget=forms.Textarea)

	