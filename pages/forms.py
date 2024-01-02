from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import *
class CreateUserForm(UserCreationForm) : 
    class Meta : 
        model = User
        fields= ['username', 'email', 'password1', 'password2']

# class Profile(forms.ModelForm) :
#     class Meta : 
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'telephone', 'specialite']

class reservations(forms.ModelForm) : 
    class Meta : 
        model = reservation
        fields =['dr','salle','date','time']    

class patientf(forms.ModelForm): 
    class Meta : 
        model = patient
        fields = ['nom', 'prenom', 'tel']

class rdv(forms.ModelForm) : 
    class Meta :  
        model = rendezvous 
        fields = ['nom','prenom','num' ,'medecin' ,'date' ,'raison']

class infermierf(forms.ModelForm) :
    class Meta : 
        model = profilI
        fields = ['user','nom', 'prenom', 'specialite']

class fiche(forms.ModelForm) : 
    class Meta : 
        model = FicheP
        fields = ['nom', 'prenom', 'patient', 'date', 'desc']
        
# class rh(forms.ModelForm)