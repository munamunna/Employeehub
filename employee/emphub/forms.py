from django import forms
from .models import Employee, Project
import re
from django.core.exceptions import ValidationError

class EmployeeForm(forms.ModelForm):
    # Define the projects field here
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        required=False,  # Allows selecting zero projects
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for selection
    )

    class Meta:
        model = Employee
        fields = "__all__"

        labels = {
        'employee_number': 'Employee Number',
        'first_name': "First Name",
        'last_name': 'Last Name',
        'email': 'Email',
        'mobile_number':'Mobile Number',
        'user':"User",
        'department':"Department",
        'position':"Position",
        
    }

        widgets = {
        'employee_number': forms.NumberInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'mobile_number':forms.TextInput(attrs={'class': 'form-control'}),
        'user':forms.Select(attrs={'class': 'form-control'}),
        'department':forms.Select(attrs={'class': 'form-control'}),
        'position':forms.Select(attrs={'class': 'form-control'}),
        
    }

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        
        # Define the expected mobile number format using a regular expression
        expected_format = r'^\+91\s\d{10}$'
        
        if not re.match(expected_format, mobile_number):
            raise ValidationError('Mobile number must start with "+91" followed by 10 digits.')

        return mobile_number