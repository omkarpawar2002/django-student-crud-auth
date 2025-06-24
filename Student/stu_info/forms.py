from django import forms
from .models import Students

gender_choice = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

subject_choice = [
    ('PHYSICS','PHYSICS'),
    ('CHEMISTRY','CHEMISTRY'),
    ('BIOLOGY','BIOLOGY'),
    ('MATHS','MATHS')
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        labels = {
            'stu_id':'STUDENT ID',
            'name':'NAME',
            'city':'CITY',
            'gender':'GENDER',
            'subject':'SUBJECT',
            'address':'ADDRESS',
            'dob':'DATE OF BIRTH',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY'
        }
        widgets = {
            'gender':forms.RadioSelect(choices=gender_choice),
            'subject':forms.Select(choices=subject_choice),
            'dob':forms.DateInput(attrs={
                'type':'date'
            }),
            'address':forms.Textarea(attrs={
                'rows':'3'
            }),
            'password':forms.TextInput(attrs={
                'type':'password'
            })
        }
