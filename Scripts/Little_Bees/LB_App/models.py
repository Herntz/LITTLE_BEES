from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Children(models.Model):
    section_choices = (('Petite', 'Petite'),('Moyenne', 'Moyenne'),('Grande', 'Grande'),)
    sexe_choices = (('F', 'Feminin'),('M', 'Masculin'),)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1,choices=sexe_choices, validators=[RegexValidator(r'^[FM]$')])
    section=models.CharField(max_length=100,choices=section_choices)
    parent = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email_parent = models.EmailField()
    date_naissance = models.DateField()
    photo = models.ImageField(upload_to='upload_to')
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.nom} {self.prenom} : {self.section}  section"

class Note(models.Model):
    children = models.ForeignKey(Children, on_delete=models.CASCADE)
    note_dessin = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    note_ecriture = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    note_chant = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.children.id} - {self.children.nom} {self.children.prenom} : {self.children.section}  section"


# create a model for the contact form

class Contact(models.Model):
    nom_complet = models.CharField(max_length=200)
    email = models.EmailField()
    objet = models.CharField(max_length=100)
    message = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.nom} : email {self.email}  "

def upload_to(instance, filename):
    return f'{instance.nom_du_modele}/{timezone.now().strftime("%Y-%m-%d")}/{filename}'

  

