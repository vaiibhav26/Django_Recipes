from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() django automatically adds this field(also works as a primary key)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    # image = models.ImageField()
    # file = models.FileField()


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default= 50)

    def __str__(self) -> str:
        return self.car_name
