from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["first_name","last_name","phone"]


class UploadForm(forms.Form):
    bestand = forms.FileField(
    label='Selecteer je ABN AMRO exportbestand (.TAB)',
    )