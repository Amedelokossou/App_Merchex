from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)


# class Contact(models.Model):
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)  # Peut être email, téléphone, etc.

#     def __str__(self):
#         return f"{self.prenom} {self.nom}"