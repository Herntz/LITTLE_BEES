from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Déconnexion de l'utilisateur
        response = super().dispatch(request, *args, **kwargs)
        # Redirection vers l'interface "index" de votre projet
        return HttpResponseRedirect(reverse_lazy('index'))  # Remplacez 'index' par le nom de votre vue "index"
