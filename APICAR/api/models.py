from django.db import models

# Create your models here.

# User
class Rol(models.Model):
    idRol = models.IntegerField(primary_key=True,db_column="idRol")
    nameRol = models.CharField(max_length=100,db_column="nameRol")
    class Meta:
        db_table = "roles"

class Gender(models.Model):
    idGender = models.IntegerField(primary_key=True,db_column="idGender")
    nameGender = models.CharField(max_length=100,db_column="nameGender")
    class Meta:
        db_table = "genders"

class Profile(models.Model):
    idUser = models.IntegerField(primary_key=True,db_column="idUser")
    nameUser = models.CharField(max_length=100,db_column="nameUser")
    emailUser = models.EmailField(unique=True,db_column="emailUser")
    passwordUser = models.CharField(max_length=255,db_column="passwordUser")
    class Meta:
        db_table = "profiles"

class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True,db_column="idProduct")
    nameProduct = models.CharField(max_length=100,db_column="nameProduct")
    priceProduct = models.FloatField(default=0,db_column="priceProduct")
    class Meta:
        db_table = "products"