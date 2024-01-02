from django.shortcuts import render, redirect
from .models import Salle
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Medecin, reservation,patient, rendezvous
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

def group_required(group_name):
    def decorator(view_func):
        def check_group(user):
            return user.groups.filter(name=group_name).exists()
        
        decorated_view = user_passes_test(check_group, login_url='login')
        return decorated_view(view_func)
    
    return decorator

def index(request) : 
    return render(request,'main/acueil.html')
@csrf_exempt
def loginU(request) : 
    if request.method =='POST' : 
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request,user)
            if user.groups.filter(name='Medecins').exists():
                return redirect('medecin')
            
            elif user.groups.filter(name='Infermier') : 
                return redirect('infermier')
            else : 
                return redirect('patient')
    return render(request, 'main/login.html')

def signup(request) : 
    form = CreateUserForm()
    if request.method =='POST' : 
        form = CreateUserForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'main/signup.html', context)


def logoutU(request) : 
    logout(request)
    return redirect('login')

@group_required('Medecins')
@login_required(login_url='login')
def medecin (request) : 
    res = reservation.objects.all()
    med = Medecin.objects.all()

    return render(request, 'medecin/medcin.html', {'medcin':med, 'res':res})

@group_required('Medecins')
@login_required(login_url='login')
def salles(request) :
    form = reservations(request.POST)
    if request.method =='POST' : 
        form = reservations(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medecin')
    return render(request, 'medecin/salles.html',{'salle':Salle.objects.all(), 'form':form})

@group_required('Medecins')
@login_required(login_url='login')
def consultation(request) : 
    medecin_instance = request.user.medecin
    rdv = rendezvous.objects.filter(medecin=medecin_instance)
    return render(request, 'medecin/consultation.html',{'rdv':rdv})


@csrf_exempt
@group_required('Medecins')
@login_required(login_url='login')
def profil(request):
    form = MedecinForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = MedecinForm(request.POST, request.FILES)
        if form.is_valid():
            medecin=form.save(commit=False)
            medecin.user = request.user
            medecin.save()
            return redirect('medecin')
        else:
            print(form.cleaned_data) 
            print(form.errors)
    context ={'form': form,'Med':Medecin}
    return render(request, 'medecin/profil.html', context)

#patient : 
@login_required(login_url='login')
def patientt(request) : 
    med = Medecin.objects.all()
    return render(request, 'client/client.html', {'med':med})

@login_required(login_url='login')
def rendezvouss(request) : 
    form = rdv(request.POST,) 
    if request.method =='POST' : 
        form = rdv(request.POST,)
        if form.is_valid() :
            form.save()
            return redirect('patient') 

    return render(request, 'client/Rdv.html',{'form':form})

@login_required(login_url='login')
def profilc(request) : 
    form = patientf(request.POST,)
    if request.method == 'POST':
        form =patientf(request.POST,)
        if form.is_valid():
            patient_instance = form.save(commit=False)
            patient_instance.usr = request.user
            patient_instance.save()
            return redirect('patient')
        else:
            print(form.cleaned_data) 
            print(form.errors)
    context ={'form': form,'patient':patient}
    return render(request,'client/prf.html',context)

#infermier
@group_required('Infermier')
@login_required(login_url='login')
def infermier(request) : 
    context = Medecin.objects.all()
    reser = reservation.objects.all()
    return render(request, 'infermier/infermier.html', {'med' : context, 'res':reser} )

@group_required('Infermier')
@login_required(login_url='login')
def salleI(request) : 
    salles = Salle.objects.all()
    form = reservations(request.POST) 
    if request.method =='POST' : 
        form = reservations(request.POST) 
        if form.is_valid :
            form.save()
            return redirect('infermier')
    return render(request, 'infermier/salles.html', {'salles': salles, 'form': form})

@group_required('Infermier')
@login_required(login_url='login')
def consultationI(request) : 
    rdv = rendezvous.objects.all()
    return render(request, 'infermier/consultation.html', {'rdv': rdv})

@group_required('Infermier')
@login_required(login_url='login')
def ficheP(request) : 
    form= fiche(request.POST) 
    if request.method =='POST' :
        form =  form= fiche(request.POST)
        if form.is_valid : 
            form.save()
            return redirect('infermier') 
    return render(request, 'infermier/fiche.html',{'form': form})

@group_required('Infermier')
@login_required(login_url='login')
def profili(request) : 
    form= infermierf(request.POST) 
    if request.method =='POST' :
        form =  form= infermierf(request.POST)
        if form.is_valid : 
            form.save()
            return redirect('infermier') 
    return render(request, 'infermier/profil.html', {'form': form})
def rh(request) : 
    return render(request, 'RH/rh.html')