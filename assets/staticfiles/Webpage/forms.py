from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UploadedImage,Emp_details,Skill

GENDER_CHOICES = [('Male','Male'),('Female','Female')]
SKILL_CHOICES = [('AWS','AWS'),('DevOps','DevOps'),('FullStackDeveloper','Full Stack Developer'),('Middleware','Middleware'),('QA-Automation','QA-Automation'),('WebServices','WebServices')]

# Signup Form
class Signupform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data

# Upload Image Form
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

# Employee Details Form
class EmployeeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Emp_details
        fields = ['firstname','lastname','email','mobile','birth','gender','address','country','city','skills']
        labels = {'firstname':'First Name','lastname':'Last Name','email':'Email ID','mobile':'Mobile Number','birth':'Date of Birth',
                  'gender':'Gender','address':'Address','country':'Country','city':'City','skills':'Skills'}
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'birth':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'country':forms.Select(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
        }