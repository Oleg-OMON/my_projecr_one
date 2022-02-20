from django import forms
from .models import AdvUser


class ChangesUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес Электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'send_messages')
