from django.contrib import admin
from django import forms
from .models import Email

class EmailAdminForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = '__all__'


class EmailAdmin(admin.ModelAdmin):
    form = EmailAdminForm
    list_display = ['message', 'subject', 'date', 'fromEmail', 'toEmail', 'isArchived']

admin.site.register(Email, EmailAdmin)

