#urls.py principal

"""
URL configuration for GuiSbeghen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from autenticad import views as autenticad_views  # Importação das views do app autenticad


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Adiciona o subapp home
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # autenticad
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'), # autenticad
    path('register/', autenticad_views.register, name='register'), # autendicad
    
    # Adicione suas outras URLs aqui
]



# Adiciona o código para servir arquivos de mídia apenas em modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
