from django.db import models

# Create your models here.
class Set1(models.Model):
  id=models.AutoField(primary_key=True)
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set1')
  
class Set2(models.Model):
  id=models.AutoField(primary_key=True)
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set2')

class Set3(models.Model):
  id=models.AutoField(primary_key=True)
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set3')

class Set4(models.Model):
  id=models.AutoField(primary_key=True)
  packagnumber=models.IntegerField()
  district=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  pricerequired=models.IntegerField()
  timerequired=models.IntegerField()
  img=models.ImageField(upload_to='set4')

class Packageset(models.Model):
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagnumber=models.IntegerField()
  location=models.CharField(max_length=100)
  spotnumber=models.IntegerField()
  spotname=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  cafespot=models.CharField(max_length=100)
  description=models.CharField(max_length=250)
  img=models.ImageField(upload_to='packageset')