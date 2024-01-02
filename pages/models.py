from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user

# Create your models here.
class Salle(models.Model): 
    num=models.CharField(max_length=3)
    image= models.ImageField(upload_to='images/')
    description=models.TextField()
    libre=models.BooleanField(default=True)

    def __str__(self): 
        return self.num
    
class Medecin(models.Model) : 
    user =models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/image/',default="image/aaa.png", blank=True)
    nom=models.CharField(max_length=15)
    prenom= models.CharField(max_length=15)
    telephone= models.CharField(max_length=10)
    specialite= models.CharField(max_length=15)

    def __str__(self) : 
        return self.nom
    
    def save(self, request=None,*args, **kwargs):
        # if request : 
        #  current_user = get_user(request)
        #  if current_user.is_authenticated:
        #     self.user = current_user

        med_group, _ = Group.objects.get_or_create(name='Medecins')
        self.user.groups.add(med_group)
        super().save(*args, **kwargs)

class ReservationCounter(models.Model):
    count = models.PositiveIntegerField(default=0)

class reservation(models.Model) :
    dr = models.OneToOneField(Medecin,null=True, on_delete=models.CASCADE)
    salle = models.OneToOneField(Salle,null=True, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    reservation_counter = models.ForeignKey(ReservationCounter, on_delete=models.SET_NULL, null=True)
    reservation_number = models.CharField(null=True,max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.reservation_counter:
            counter, created = ReservationCounter.objects.get_or_create(pk=1)
            self.reservation_counter = counter
            self.reservation_number = str(counter.count + 1)
            counter.count += 1
            counter.save()
        super().save(*args, **kwargs)

@receiver(post_save, sender=reservation)
def update_salle_libre(sender, instance, created, **kwargs):
    if created:
        instance.salle.libre = False
        instance.salle.save()

#Patient 
class patient(models.Model) : 
    usr = models.OneToOneField(User,on_delete=models.CASCADE,limit_choices_to={'groups__isnull': True})
    prf = models.ImageField(upload_to='media/image/',default="image/aaa.png", blank=True)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    tel = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self): 
        return self.nom

    def save(self, *args, **kwargs):
        client_group, _ = Group.objects.get_or_create(name='Client')
        self.usr.groups.add(client_group)
        super().save(*args, **kwargs)

class rendezvous(models.Model) : 
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    num = models.CharField(null=True,max_length=10)
    medecin= models.ManyToManyField(Medecin)
    date = models.DateTimeField(null=False)
    raison = models.CharField(null=True, max_length=50)

    def __str__(self): 
        return self.nom

    def save(self, *args, **kwargs ) : 
        super().save(*args, **kwargs )

#la fiche patient : 

class FicheP(models.Model) : 
    patient = models.OneToOneField(patient,on_delete=models.CASCADE)
    nom = models.CharField(max_length=15, null=True)
    prenom = models.CharField(max_length=15)
    tel= models.CharField(max_length=15)
    date = models.DateTimeField()
    desc = models.CharField(max_length=15)
    
    def __str__(self) : 
        return self.nom

#profile Infermier  

class profilI(models.Model) : 
    nom = models.CharField(max_length=15, null=True)
    prenom = models.CharField(max_length=15, null=True)
    specialite = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    prf = models.ImageField(upload_to='media/image/', default="image/aaa.png", blank=True)

    def __str__(self): 
        return self.nom

    # def save(self, *args, **kwargs):
    #     med_group, _ = Group.objects.get_or_create(name='Infermier')
    #     self.user.groups.add(med_group)
    #     super().save(*args, **kwargs)

# class Rh(models.Model) : 
#     def creeruser(self, username,password, **extra_fields) :
#         user = self.model(username= username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create

# class CustomUserManager(models.Manager):
#     def create_user(self, username, password, **extra_fields):
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)

# class CustomUser(User):
#     # Ajoutez des champs personnalisés ici si nécessaire
#     objects = CustomUserManager()

# class CustomGroup(Group):
#     pass