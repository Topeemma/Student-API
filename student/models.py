from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)
    level = models.IntegerField()
    
    
    def __str__(self):
        return self.firstname
