from django import forms
from django.contrib.auth.forms import SetPasswordForm as BaseSetPasswordForm


class ForgotPasswordForm(forms.Form):
    contact = forms.CharField(label='Enter your mobile number or email address', max_length=100)

    def clean_contact(self):
        contact = self.cleaned_data['contact']
        # Validate whether the input is an email or a valid phone number
        if '@' in contact:  # Assuming '@' indicates it's an email
            return contact
        elif contact.isdigit() and len(contact) >= 10:  # Assuming a valid phone number is at least 10 digits
            return contact
        else:
            raise forms.ValidationError("Please enter a valid email address or phone number.")


class SetPasswordForm(BaseSetPasswordForm):
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
