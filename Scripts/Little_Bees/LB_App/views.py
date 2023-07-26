from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import ContactForm
from django.contrib import messages

def index(request):
    template = loader.get_template('themes/index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('themes/about.html')
    return HttpResponse(template.render())
def classes(request):
    template = loader.get_template('themes/classes.html')
    return HttpResponse(template.render())
def gallery(request):
    template = loader.get_template('themes/gallery.html')
    return HttpResponse(template.render())

def infos_utiles(request):
    all_children = Children.objects.all()
    selected_child_id = request.POST.get('selected_child_id')
    if selected_child_id:
        selected_child = Children.objects.get(id=selected_child_id)
    else:
        selected_child = None
    # Compter le nombre d'enfants pour chaque section
    nombre_enfants_tous = all_children.count()
    nombre_enfants_petite = all_children.filter(section="Petite").count()
    nombre_enfants_moyenne = all_children.filter(section="Moyenne").count()
    nombre_enfants_grande = all_children.filter(section="Grande").count()

    context = {
        'all_children': all_children,
        'selected_child': selected_child,
        'nombre_enfants_tous': nombre_enfants_tous,
        'nombre_enfants_petite': nombre_enfants_petite,
        'nombre_enfants_moyenne': nombre_enfants_moyenne,
        'nombre_enfants_grande': nombre_enfants_grande
    }

    template = loader.get_template('themes/infos_utiles.html')
    return HttpResponse(template.render(context, request))

def tri_mention_table(request):
    val = request.GET.get('mention', 'tous')
    
    all_children = Children.objects.all()

    for child in all_children:
        # Récupérer les notes du modèle Note pour chaque enfant
        notes = Note.objects.filter(children=child)
        notes_list = [note.note_dessin for note in notes if note.note_dessin is not None] + \
                     [note.note_ecriture for note in notes if note.note_ecriture is not None] + \
                     [note.note_chant for note in notes if note.note_chant is not None]
        average = round(sum(notes_list) / len(notes_list), 2) if notes_list else 0

        if notes_list:
            if average >= 6:
                mention = "Accepter"
                status = "delivered"  # Couleur verte pour la mention "Accepter"
            else:
                mention = "Refuser"
                status = "cancelled"  # Couleur rouge pour la mention "Refuser"
        else:
            average = 0
            mention = "Aucune note"
            status = "pending"

        # Ajouter les attributs 'average', 'mention', et 'color' à l'objet Children
        child.average = average
        child.mention = mention
        child.status = status

    # Tri des enfants par ordre décroissant de la moyenne
    sorted_children = sorted(all_children, key=lambda x: x.average, reverse=True)

    if val != "tous":
        sorted_children = [child for child in sorted_children if child.mention == val]

    context = {
        'children': sorted_children,
    }
    return render(request, 'themes/table_trier_mention.html', context)


def tri_enfants_table(request):
    section = request.GET.get('section', 'tous')
    all_children = Children.objects.all()

    if section != "tous":
        all_children = all_children.filter(section=section)
    else:
        all_children=all_children
    selected_child_id = request.POST.get('selected_child_id')
    if selected_child_id:
        selected_child = Children.objects.get(id=selected_child_id)
    else:
        selected_child = None

    context = {
        'all_children': all_children,
        'selected_child': selected_child,
    }

    return render(request, 'themes/table_trier_section.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message a été envoyé avec succès!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'themes/contact.html', {'form': form})


def resultats(request):
    # Récupérer tous les enfants
    children = Children.objects.all()

    for child in children:
        # Récupérer les notes du modèle Note pour chaque enfant
        notes = Note.objects.filter(children=child)
        notes_list = [note.note_dessin for note in notes if note.note_dessin is not None] + \
                     [note.note_ecriture for note in notes if note.note_ecriture is not None] + \
                     [note.note_chant for note in notes if note.note_chant is not None]
        average = round(sum(notes_list) / len(notes_list), 2) if notes_list else 0

        if notes_list:
            
            if average >= 6:
                mention = "Accepter"
                status = "delivered"  # Couleur verte pour la mention "Accepter"
            else:
                mention = "Refuser"
                status = "cancelled"  # Couleur rouge pour la mention "Refuser"
        else:
            average = 0
            mention = "Aucune note"
            status = "pending"

        # Ajouter les attributs 'average', 'mention', et 'color' à l'objet Children
        child.average = average
        child.mention = mention
        child.status = status
    # Compter le nombre d'enfants pour chaque section
    nombre_enfants_tous = children.count()
    nombre_enfants_accepter = 0
    nombre_enfants_refuser = 0
    nombre_enfants_aucune = 0

    for child in children:
        if child.mention == "Accepter":
            nombre_enfants_accepter += 1
        elif child.mention == "Refuser":
            nombre_enfants_refuser += 1
        elif child.mention == "Aucune note":
            nombre_enfants_aucune += 1
    # Tri des enfants par ordre décroissant de la moyenne
    children = sorted(children, key=lambda x: x.average, reverse=True)

    # Transmettre les données au template HTML sous forme de dictionnaire
    context = {
        'children': children,
        'nombre_enfants_tous': nombre_enfants_tous,
        'nombre_enfants_accepter': nombre_enfants_accepter,
        'nombre_enfants_refuser': nombre_enfants_refuser,
        'nombre_enfants_aucune': nombre_enfants_aucune,
    }
    template = loader.get_template('themes/resultats.html')
    return HttpResponse(template.render(context, request))

def call_to_action(request):
    all_children  = Children.objects.all()
    
    template = loader.get_template('themes/call-to-action.html')
    context = {
        'all_children': all_children,
        }
    
    return HttpResponse(template.render(context,request))

