# autenticad/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileEditForm  # Certifique-se de que UserProfileEditForm é o correto
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    """Handle user registration and automatic login after successful registration."""    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Encrypt the password
            user.save()
            login(request, user)
            messages.success(request, 'Registro bem-sucedido! Você agora está logado.')
            return redirect('/home/')  # Redirecionamento direto
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def perfil(request):
    """Display user profile information."""
    user = request.user

    context = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': getattr(user, 'age', None),
        'birth_date': getattr(user, 'birth_date', None),
        'city': getattr(user, 'city', None),
        'state': getattr(user, 'state', None),
        'address': getattr(user, 'address', None),
        'whatsapp': getattr(user, 'whatsapp', None),
        'avatar': getattr(user, 'avatar', None),
        'biography': getattr(user, 'biography', None),
        'nickname': getattr(user, 'nickname', None),
    }

    return render(request, 'autenticad/perfil.html', context)  # Renderiza o template com os dados do contexto

@login_required
def editar_perfil(request):
    """Edit user profile information."""
    user = request.user

    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=user)  # Formulário de edição
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')  # Redireciona para a página do perfil após salvar
    else:
        form = UserProfileEditForm(instance=user)  # Preenche o formulário com os dados do usuário existente

    return render(request, 'autenticad/editar_perfil.html', {'form': form, 'username': user.username})

