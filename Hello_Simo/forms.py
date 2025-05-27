from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'enrolled']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
        }
        labels = {
            'name': 'Full Name',
            'age': 'Student Age',
            'enrolled': 'Is Enrolled?'
        }
        help_texts = {
            'age': 'Age must be greater than 0',
        }

    # 👇 custom field validation
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return age
