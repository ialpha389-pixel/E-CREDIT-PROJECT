from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    nom_complet= models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    revenuMensuel = models.DecimalField()
    employeur = models.CharField(max_length=200)
    telephone = models.CharField(max_length=13,unique=True)
    genre = models.CharField(max_length=1)
    adresse = models.TextField()
    date_naissance = models.DateField()
    date_creation = models.DateTimeField()

    def __str__(self):
        return f"{self.nom_complet} | {self.genre} | {self.genre} | {self.adresse}"

class Compte(models.Model):
    id = models.IntegerField(primary_key=True)
    numero = models.CharField(max_length=10)
    solde = models.DecimalField()
    date_creation = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
TYPE_TRANS_CHOICES = (('retrait','retrait'), ('depot', 'depot'),)

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    montant = models.DecimalField()
    type = models.CharField(choices=TYPE_TRANS_CHOICES, default='depot', max_length=30)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
ROLES = (('AGENT_COMMERCIAL', 'AGENT_COMMERCIAL'), ('DIRECTEUR_COMMERCIAL', 'DIRECTEUR_COMMERCIAL'),)
class Agent(models.Model):
    id = models.IntegerField(primary_key=True)
    nom_complet = models.CharField(max_length=200)
    actif = models.BooleanField(default=True)
    roles = models.CharField(choices=ROLES, default='AGENT_COMMERCIAL',max_length=200)

typeCredit = (('INVEST', 'INVEST'),('ACADEMIA', 'ACADEMIA'),('SANTE', 'SANTE'),('IMMO', 'IMMO'),)
STATUSCREDIT = (('EN_ATTENTE', 'EN_ATTENTE'), ('APPROUVER','APPROUVER'),('REJETE', 'REJETE'),)
class DemandeCredit(models.Model):
    id = models.IntegerField(primary_key=True)
    montant = models.DecimalField()
    duree = models.IntegerField()
    typeCredit = models.CharField(choices=typeCredit, default='INVEST', max_length=100)
    statut = models.CharField(choices=STATUSCREDIT, default='EN_ATTENTE', max_length=100)
    date_cloture =models.DateField()
    Date_creation =models.DateTimeField()
    document = models.FileField()
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

class Remboursement(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    montant = models.DecimalField()
    demandeCredit = models.ForeignKey(DemandeCredit,on_delete=models.CASCADE)