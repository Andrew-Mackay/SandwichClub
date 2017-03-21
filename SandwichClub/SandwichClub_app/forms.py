from django import forms
from SandwichClub_app.models import *

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)

class SandwichForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(required=False)

    class Meta:
        model = Sandwich
        exclude = ('sid','rating','created','maker')
