from django import forms
from .models import *
from django.core import validators


def look_for_z(value):
    if value[0].lower() !='z':
        raise  forms.ValidationError("Must start with 'z")

class FirstForm(forms.Form):
    name=forms.CharField(validators=[look_for_z,validators.validate_slug])
    email=forms.EmailField()
    verify_email=forms.EmailField()
    body=forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0,message="GOTCHA BOT!")])

    #def clean_botcatcher(self):
        #botcatcher = self.cleaned_data['botcatcher']
        #if len(botcatcher) > 0:
            #raise forms.ValidationError("Gotcha BOT")
        #return botcatcher
    def clean(self):
        all_cleaned_data=super().clean()

        email=all_cleaned_data['email']
        verify_email=all_cleaned_data['verify_email']

        if email[email.find('@')+1:email.find('@')+6] != 'gmail':
            raise forms.ValidationError("eamil domain must be gamil")

        if email != verify_email:
            raise forms.ValidationError("email and verify email is not match!.")
