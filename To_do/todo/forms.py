from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(min_length=3)

    class Meta:
        model = Task
        fields = ['title',]