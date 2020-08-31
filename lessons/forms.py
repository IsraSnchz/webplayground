from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['title', 'video', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'video': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Video link'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden  '}),
        }
        labels = {
            'title':'','video':'', 'order':'', 'content': ''
        }