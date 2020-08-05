from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True)
    password_confirmation = forms.CharField(min_length=8, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation',
                  'email', 'first_name', 'last_name')

    def clean(self, data):
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Пароли не совпадают')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user