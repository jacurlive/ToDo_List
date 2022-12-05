from django import forms
from task.models import Task


class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class CompleteTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('complete',)
