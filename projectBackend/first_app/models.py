from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    father_name = models.TextField()
    mother_name = models.TextField()
    Address = models.TextField()
    def __str__(self) -> str:
        return f'Name : {self.name}'

