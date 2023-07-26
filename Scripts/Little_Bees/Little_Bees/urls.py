"""
URL configuration for Little_Bees project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import CustomLogoutView  # Importez la vue personnalisée

admin.site.site_url = "http://localhost:8000/admin"
admin.site.site_header = "Little Bees Admin"
admin.site.site_title = "Little Bees Admin Portail"
admin.site.index_title = "Bienvenue sur Little Bees Admin Portail"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # Cette ligne gère les URL d'authentification
    path('',include('LB_App.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)