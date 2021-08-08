from django import forms


class CreateSchool(forms.Form):
    school_name = forms.CharField(label="School Name", max_length=255)
