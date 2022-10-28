from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism=models.CharField(max_length=50)
    yosh=models.PositiveIntegerField()
    kasb=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Maqola(models.Model):
    sarlavha=models.TextField()
    sana=models.DateField()
    mavzu=models.TextField()
    matn=models.TextField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
