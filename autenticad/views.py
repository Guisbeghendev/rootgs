from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        age = request.POST.get('age')
        birth_date = request.POST.get('birth_date')
        city = request.POST.get('city')
        state = request.POST.get('state')
        address = request.POST.get('address')
        whatsapp = request.POST.get('whatsapp')
        avatar = request.FILES.get('avatar')
        biography = request.POST.get('biography')
        nickname = request.POST.get('nickname')

        # Cria um novo usuário
        try:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.first_name = full_name
            user.save()
            # Aqui você pode adicionar a lógica para salvar as informações opcionais em um modelo separado se desejar

            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('login')  # Redireciona para a página de login após o registro
        except Exception as e:
            messages.error(request, f'Erro ao registrar: {e}')

    return render(request, 'registration/register.html')

