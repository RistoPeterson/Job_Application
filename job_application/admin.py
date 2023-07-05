from django.contrib import admin
from .models import Form, ContactForm


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "email", "date", "occupation")
    list_filter = ("date", "occupation")
    ordering = ("first_name",)
    readonly_fields = ("occupation",)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "comments")
    search_fields = ("full_name", "email")
    ordering = ("full_name",)
    readonly_fields = ("comments",)


# Register your models here.
admin.site.register(Form, FormAdmin)
admin.site.register(ContactForm, CommentsAdmin)
