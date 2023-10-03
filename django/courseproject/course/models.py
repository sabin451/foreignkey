from django.db import models

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=255,null=True)
    fee=models.IntegerField(null=True)
class student(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    sname=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField(null=True,blank=True,default=1)
    date=models.DateField()