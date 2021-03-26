from django import forms

class jsonForm(forms.Form):

    file = forms.FileField(allow_empty_file="false")