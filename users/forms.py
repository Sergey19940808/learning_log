# imports
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



# class web-form email
class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        labels = {'email': ''}


    # validate email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Адрес уже используется, введите другой, к которому у вас есть доступ')
        elif len(email) > 50:
            raise ValidationError('Слишком длинный адресс электронной почты.')
        elif len(email) < 15:
            raise ValidationError('Слишком короткий электронный адрес.')
        else:
            return email


# class web-form for first_name
class FirstNameLastNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия'}

    # validate first_name
    def clean_firstname(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name[:2]:
            raise ValidationError('Слишком короткое имя.')
        else:
            return first_name

    # validate last_name
    def clean_lastname(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name[:3]:
            raise ValidationError('Слишком короткая фамилия.')
        else:
            return last_name





