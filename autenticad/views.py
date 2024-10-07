# autenticad/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

def register(request):
    """Handle user registration and automatic login after successful registration."""
    
    if request.method == 'POST':
        # Instantiate the registration form with POST data and files (if any).
        form = UserRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Create a user instance but do not save it to the database yet.
            user = form.save(commit=False)
            # Set the password for the user instance.
            user.set_password(form.cleaned_data['password1'])  # Encrypt the password
            # Save the user instance to the database.
            user.save()
            # Automatically log the user in after successful registration.
            login(request, user)
            messages.success(request, 'Registro bem-sucedido! Você agora está logado.')
            # Redirect to the home page or another page after registration.
            return redirect('home')
    else:
        # If the request is not POST, instantiate a new empty form.
        form = UserRegistrationForm()

    # Render the registration template with the form.
    return render(request, 'registration/register.html', {'form': form})
