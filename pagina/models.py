from django.db import models

# Create your models here.
class messages(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='name')
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500, verbose_name='message')