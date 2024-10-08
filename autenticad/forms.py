# autenticad/forms.py

from django import forms
from .models import UserExtended  # Importe o UserExtended

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    class Meta:
        model = UserExtended
        fields = ['username', 'email', 'password1', 'password2', 
                  'age', 'birth_date', 'city', 'state', 
                  'address', 'whatsapp', 'avatar', 'biography', 'me_conhece_como']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem")
        return password2


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = [
            'first_name',
            'last_name',
            'age',
            'birth_date',
            'city',
            'state',
            'address',
            'whatsapp',
            'avatar',
            'biography',
            'me_conhece_como',
        ]
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'age': 'Idade',
            'birth_date': 'Data de Nascimento',
            'city': 'Cidade',
            'state': 'Estado',
            'address': 'Endereço',
            'whatsapp': 'WhatsApp',
            'avatar': 'Foto para Avatar',
            'biography': 'Biografia',
            'me_conhece_como': 'Como você me conhece?',  
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserExtended.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    # Se você precisar de validações personalizadas adicionais, adicione aqui.
