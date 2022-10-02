
from logging import PlaceHolder
from pyexpat import model
from tkinter import Place
from django import forms 
from .models import Task
import datetime

class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields = ['title', 'description', 'duedate', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write a description'}),
            'duedate': forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'duedate (yyyy-mm-dd)'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
                }
