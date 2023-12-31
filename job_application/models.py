from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactForm(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    comments = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.full_name}"

