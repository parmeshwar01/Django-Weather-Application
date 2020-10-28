from django.db import models

# Create your models here.


class City(models.Model):
    city_id = models.AutoField
    name =models.CharField(max_length=122)

    def __str__(self):
        return self.name
