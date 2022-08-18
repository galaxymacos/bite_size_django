from django import forms


class NameForm(forms.Form):
    # setting max_length in forms can "prevent HTML too long" and "validate data back to the server"
    your_name = forms.CharField(label="Your name", max_length=100)
