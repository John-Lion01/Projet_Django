# from django.db import models

# Create your models here.
from django.db import models

class Reponse(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    commentaire = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
