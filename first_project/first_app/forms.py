from django import forms
# from django.core import validators
from first_app.models import Webpage

from django.contrib.auth.models import User
from .models import UserProfileInfo

class NewWebpageForm(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')



# def check_name_must_start_with_letter_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with Z")

# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again:')
#     text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     verimail = all_clean_data['verify_email']

    #     if email != verimail:
    #         raise forms.ValidationError("MAKE SURE EMAILS MATCH!")


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher