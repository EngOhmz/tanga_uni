from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMessage, Donation

# class MemberRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = ['full_name', 'email', 'phone', 'member_type', 'university_name', 'living_place', 'address']

#     def __init__(self, *args, **kwargs):
#         super(MemberRegistrationForm, self).__init__(*args, **kwargs)
#         self.fields['university_name'].required = False
#         self.fields['address'].required = False




# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'amount', 'message']


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 5}), required=True)


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'full_name', 'email', 'phone', 'member_type',
            'university_name', 'living_place', 'address'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
        }

    def clean(self):
        cleaned_data = super().clean()
        member_type = cleaned_data.get('member_type')
        university_name = cleaned_data.get('university_name')

        if member_type == 'university_member' and not university_name:
            self.add_error('university_name', 'University name is required for university members.')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or not phone.startswith('+255') or len(phone) < 10:
            raise forms.ValidationError("Enter a valid Tanzanian phone number (e.g. +2557XXXXXXX)")
        return phone