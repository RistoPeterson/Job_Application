from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    date = forms.CharField(max_length=50)
    occupation = forms.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    comments = forms.CharField(max_length=500)

    def __str__(self):
        return f"{self.full_name}"
