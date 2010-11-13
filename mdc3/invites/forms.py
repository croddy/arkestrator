from django import forms
from django.contrib.auth.models import User
from mdc3.invites.models import Invite
from mdc3.profiles.models import Profile

import datetime
import re

class NewInviteForm(forms.Form):
    """ a form to create a new invite """
    invitee = forms.EmailField(required=True, label="Email", widget=forms.TextInput(attrs={'size': 70, 'maxlength': 160}))
    explanation = forms.CharField(max_length=150,
        label="Explain",
        widget=forms.Textarea(attrs={'rows': 6, 'cols': 70}))

    def save(self, user):
        invite = Invite.objects.create(
            inviter = user,
            invitee = self.cleaned_data['invitee'],
            explanation = self.cleaned_data['explanation']
            )
        return invite

class UserRegistrationForm(forms.ModelForm):
    """ a form to register a new user """
    username = forms.CharField(max_length = 20,
            help_text = 'Required. 20 characters or fewer. Letters, numbers and @/./+/-/_ characters')
    class Meta:
        model = User
        fields = ('username', 'email')
    
    pass1 = forms.CharField(required=True,
            label="Password",
            widget=forms.PasswordInput)
    pass2 = forms.CharField(required=True,
            label="Password (confirm)",
            widget=forms.PasswordInput)

    #don't allow whitespace in usernames
    def clean_username(self):
        """ make sure there is no whitespace in usernames """
        if re.search(r'\s', self.cleaned_data['username']):
            raise forms.ValidationError(
                    "No whitespace is allowed in usernames. Perhaps you'd like to use an _")
        return self.cleaned_data['username']

    def clean(self):
        """ verify that both passwords match """
        if self.cleaned_data["pass1"] != self.cleaned_data["pass2"]:
            raise forms.ValidationError("Passwords don't match.")
        return self.cleaned_data

class ProfileRegistrationForm(forms.ModelForm):
    """ the profile part of registration """
    class Meta:
        model = Profile
        fields = ('name', 'location')

        


    
