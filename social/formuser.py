from django import forms
from .models import UserProfile, Workplace, Education

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_picture', 'bio', 'location', 'website', 'birth_date', 'gender', 'workplaces', 'educations']
        widgets = {
            'workplaces': forms.CheckboxSelectMultiple,
            'educations': forms.CheckboxSelectMultiple,
        }

class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = ['name']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['name']
