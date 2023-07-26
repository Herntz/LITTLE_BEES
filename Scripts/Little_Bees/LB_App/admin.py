from django.contrib import admin
from .models import *


@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom','section','date_naissance',
                    'sexe', 'parent','tel','email_parent') 
    list_filter = ('section', 'sexe')
    search_fields = ('nom', 'prenom', 'parent')



@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('children',  'note_dessin','note_ecriture','note_chant')
    list_filter = ( 'children__sexe', 'children__section')
    search_fields = ('children__nom', 'children__prenom', 'cours__nom')
     
    def children__section(self, obj):
        return obj.children.section  # Permet d'afficher la section de l'enfant dans la liste des notes
    children__section.short_description = 'Section'
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "children":
            # Filtrer les enfants qui n'ont pas déjà deux notes associées
            kwargs["queryset"] = Children.objects.annotate(num_notes=models.Count('note')).filter(num_notes__lt=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Contact)  
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_complet', 'email', 'objet', 'message')
    list_display_links = ('id', 'nom_complet')
    search_fields = ('nom_complet', 'email', 'objet')
    list_per_page = 25
