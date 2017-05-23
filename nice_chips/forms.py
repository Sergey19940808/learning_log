# imports
from django import forms
from .models import Draft, Reminder

# class web-form for mydraft
class DraftForm(forms.ModelForm):
    class Meta:
        model = Draft
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}



# class web-form for my reminder
class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['name', 'text', 'date_is_up']
        labels = {'name': 'Имя напоминания', 'text': 'Описание напоминания',
                  'date_is_up': 'Время наступления события'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}