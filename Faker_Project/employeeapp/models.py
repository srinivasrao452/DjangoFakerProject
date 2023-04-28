
from django.db import models
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    salary = models.FloatField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    