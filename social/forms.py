from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import UserProfile


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    birth_date = forms.DateField(label='Date of Birth', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'confirm_password', 'birth_date', 'gender')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        # Create the User instance first
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        # Create the UserProfile instance and associate it with the User
        user_profile = UserProfile(
            user=user,
            birth_date=self.cleaned_data['birth_date'],
            gender=self.cleaned_data['gender']
        )

        if commit:
            user.save()  # Save the User instance to the database
            user_profile.save()  # Save the UserProfile instance to the database

        return user  # Return the created User instance


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
