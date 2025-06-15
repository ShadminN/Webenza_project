from django import forms
from django.core.validators import RegexValidator
from .models import Contact
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'John Doe'}),
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z\s]+$',
                message='Name should contain letters and spaces only.'
            )
        ]
    )
        
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'example@example.com'})
    )
    phone = forms.IntegerField(
        required=False,
        label='Phone Number',
        widget=forms.NumberInput(attrs={
            'placeholder': '1234567890',
            'min': '1000000000',  # Minimum 10 digits
            'max': '9999999999'   # Adjust as needed (10 digits example)
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message here...'}),
        label='Message',
        max_length=2000
    )

    captcha = ReCaptchaField()  # Add reCAPTCHA field
    
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and (phone < 1000000000 or phone > 9999999999):
            raise forms.ValidationError('Enter a valid phone number with 10 digits.')
        return phone
    




    
