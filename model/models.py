from email.mime import image
from django.db import models

class PJ(models.Model):
    img=models.ImageField(upload_to='')