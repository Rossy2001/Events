from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=150,default='')
    message=models.TextField(max_length=150)
    def __str__(self):
        return self.name

class Event(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,editable = False)
    Event_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.name

class Bharatanatyam_Event(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.name

class Painting_Event(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.name

class Mohiniyattam_Event(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.name

class Mime_Event(models.Model):
    sno=models.AutoField(primary_key=True)
    Group_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.Group_name

class Groupsong_Event(models.Model):
    sno=models.AutoField(primary_key=True)
    Group_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.Group_name

class Groupdance_Event(models.Model):
    sno=models.AutoField(primary_key=True)
    Group_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.Group_name