from django import forms
from .models import Task
class CreateNewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'project': forms.Select(attrs={'class': 'form-select'}),
        }

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyect", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))