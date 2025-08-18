from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    confirm_password = forms.PasswordInput(required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]

    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("Parollar ikki xil!")
        return data["password_2"]


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label="Parolni takrorlang", widget=forms.PasswordInput)
