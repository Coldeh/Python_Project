from django.contrib.auth.models import Group

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CreateVendor(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            client_group = Group.objects.get(name='Vendor')
            user.groups.add(client_group)
        return user