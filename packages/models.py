from django.db import models

# Create your models here.
class Set1(models.Model):
  sno=models.IntegerField()
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set1')
  
class Set2(models.Model):
  sno=models.IntegerField()
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set2')

class Set3(models.Model):
  sno=models.IntegerField()
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set3')

class Set4(models.Model):
  sno=models.IntegerField()
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set4')