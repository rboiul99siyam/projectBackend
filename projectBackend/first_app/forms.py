from django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name':'Student Name',
        }
        widgets = {
            'father_name':forms.TextInput(),
            'mother_name':forms.TextInput(),
            'Address':forms.TextInput(),
        }
    