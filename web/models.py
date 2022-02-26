from django.db import models

class comments(models.Model):
    email= models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    is_positive= models.BooleanField(default=False)
    class Meta:
        db_table='chat'


# Create your models here.
