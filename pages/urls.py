from django.urls import path
from . import views

urlpatterns=[
    # home pages
    path('',views.index, name='index'),
    path('login', views.loginU, name='login'),
    path('signup', views.signup,name='signup'), 
    path('logout', views.logoutU,name='logout'),
    # interface medecin :
    path('medecin', views.medecin, name='medecin'),
    path('salles', views.salles, name='salles'),
    path('consultation', views.consultation, name='consultation'),
    path('profil', views.profil, name='profil'),
    #interface client : 
    path('patient',views.patientt, name='patient'),
    path('rendezvous', views.rendezvouss, name='rendezvous'),
    path('profilc',views.profilc, name='profilc'),
    #interface infermier : 
    path('infermier', views.infermier,name='infermier'), 
    path('sallesI', views.salleI,name='sallesI'),
    path('consultationI', views.consultationI, name='consultationI'), 
    path('fichepatient', views.ficheP, name='fichepatient'), 
    path('profilI', views.profili, name='profilI'),
    #rh  
    path('RH', views.rh, name='RH')
]
