from datetime import date
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'due_date', 'priority_level', 'finished']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'value': date.today().strftime("%Y-%m-%d"),
                                               'placeholder': 'YYYY-MM-DD'}),
            'priority_level': forms.NumberInput(attrs={'class': 'form-control', 'value': 1, 'min': 1, 'max': 5}),
            'finished': forms.CheckboxInput(attrs={'class': 'form-check-inline form-check-input'})
        }
        labels = {
            'content': '할 일',
            'due_date': '기한',
            'priority_level': '중요도',
            'finished': '완료함',
        }
