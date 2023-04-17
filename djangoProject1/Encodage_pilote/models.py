import datetime

from django.db import models

# Create your models here.
class Personne(models.Model):
    id_personne = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField(default=datetime.date.today)
    lieu_naissance = models.CharField(max_length=255)
    alive = models.BooleanField(default=True)
    telephone = models.IntegerField(default=2)
    gsm = models.IntegerField(default=3)
    mail = models.EmailField(null=True, blank=True)
    niss = models.BooleanField(default=True)
    ville = models.ForeignKey('Adresse', on_delete=models.CASCADE,default="Mons")
    idclub = models.ForeignKey('Club', on_delete=models.CASCADE, default=1)
    idinscription = models.ForeignKey('Inscription', on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Vol(models.Model):
    id_vol = models.IntegerField(primary_key=True)
    date = models.DateField()
    type = models.CharField(max_length=255)
    ratio = models.FloatField()
    lancer = models.IntegerField()
    debut = models.TimeField()
    fin = models.TimeField()
    ticket = models.BooleanField()
    tn = models.CharField(max_length=255)
    remarque = models.TextField(null=True, blank=True)
    pmr = models.BooleanField()
    towplane_max_alt = models.FloatField()
    temps_moteur = models.FloatField()
    id_planeur = models.ForeignKey('Planeur', on_delete=models.CASCADE)
    implique = models.ManyToManyField('Personne')
    def __str__(self):
        return f"Vol {self.id_vol} ({self.date} - {self.type})"

class Planeur(models.Model):
    id_planeur = models.IntegerField(primary_key=True)
    immatriculation = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    prix = models.FloatField()
    biplace = models.BooleanField()
    proprietaire = models.CharField(max_length=255)
    alive = models.BooleanField()
    tmg = models.BooleanField()
    sl = models.BooleanField()
    prix_moteur = models.FloatField()
    dto = models.BooleanField()
    numerof = models.ForeignKey('Flarm', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.immatriculation} ({self.type})"


class License(models.Model):
    numerol = models.IntegerField(primary_key=True)
    emission = models.DateField()
    idtypel = models.ForeignKey('TypeLicense', on_delete=models.CASCADE)
    idpersonne = models.ForeignKey('Personne', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.numero_l}"


class Flarm(models.Model):
    numero_f = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)
    id_radio = models.CharField(max_length=20)
    id_lcc = models.CharField(max_length=20)
    firmware = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.numero_f}"


class TypePersonne(models.Model):
    id_type_p = models.IntegerField(primary_key=True)
    instr_remorque = models.BooleanField(default=False)
    instr_treuil = models.BooleanField(default=False)
    lacher_remorque = models.BooleanField(default=False)
    treuillard = models.BooleanField(default=False)
    passager = models.BooleanField(default=False)
    pilote = models.BooleanField(default=False)
    eleve = models.BooleanField(default=False)
    pilote_avion = models.BooleanField(default=False)
    pmr = models.BooleanField(default=False)
    honneur = models.BooleanField(default=False)
    peutetre = models.ManyToManyField('Personne')
    def __str__(self):
        return f"{self.id_type_p}"


class Adresse(models.Model):
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.ville}, {self.code_postal}, {self.pays}"


class Club(models.Model):
    idclub = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    alive = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Log(models.Model):
    idlog = models.AutoField(primary_key=True)
    dateheure = models.DateTimeField(auto_now_add=True)
    qui = models.CharField(max_length=100)
    ordinateur = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    id_personne = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idlog} - {self.qui} - {self.action}"

class Inscription(models.Model):
    idinscription = models.AutoField(primary_key=True)
    typeassurance = models.CharField(max_length=100)
    caution = models.BooleanField(default=True)
    cotisation = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    actif = models.BooleanField(default=True)
    forfait_saison = models.BooleanField(default=False)
    stage = models.BooleanField(default=False)
    fcfvv = models.BooleanField(default=False)

    def __str__(self):
        return f"Inscription {self.idinscription}"


class ContactUrgence(models.Model):
    idcontact = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    estrelie = models.ManyToManyField(Personne)
    def __str__(self):
        return f"ContactUrgence {self.idcontact}: {self.nom} {self.prenom}"

class Facture(models.Model):
    idfacture = models.AutoField(primary_key=True)
    date_facture = models.DateField()
    date_paiement = models.DateField(null=True, blank=True)
    supplement = models.DecimalField(max_digits=10, decimal_places=2)
    id_vol = models.ForeignKey(Vol, on_delete=models.CASCADE)
    def __str__(self):
        return f"Facture {self.idfacture}: {self.date_facture}"

class Lieu(models.Model):
    id_lieu = models.AutoField(primary_key=True)
    code_lieu = models.CharField(max_length=10)
    ville = models.CharField(max_length=100)
    descriptif = models.TextField()
    type = models.CharField(max_length=50)
    sepasse = models.ManyToManyField(Vol)
    def __str__(self):
        return f"Lieu {self.code_lieu}: {self.ville}"

class TypeLicense(models.Model):
    idtypel = models.AutoField(primary_key=True)
    trouillard = models.BooleanField()
    pilote = models.BooleanField()
    pilotetmg = models.BooleanField()
    piloteavion = models.BooleanField()

    class Meta:
        db_table = "typelicense"

