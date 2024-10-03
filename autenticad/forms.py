from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)
    
    # Campos Opcionais
    age = forms.IntegerField(label='Idade', required=False)
    birth_date = forms.DateField(label='Data de Nascimento', required=False)
    city = forms.CharField(label='Cidade', required=False)
    state = forms.CharField(label='Estado', required=False)
    address = forms.CharField(label='Endereço', required=False)
    whatsapp = forms.CharField(label='WhatsApp', required=False)
    avatar = forms.ImageField(label='Foto para Avatar', required=False)
    biography = forms.CharField(label='Biografia', widget=forms.Textarea, required=False)
    nickname = forms.CharField(label='Me Conhece Como?', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'birth_date', 'city', 'state', 'address', 'whatsapp', 'avatar', 'biography', 'nickname']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem")
        return password2
