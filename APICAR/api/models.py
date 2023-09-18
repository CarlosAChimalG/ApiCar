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

class User(models.Model):
    idUser = models.IntegerField(primary_key=True,db_column="idUser")
    nameUser = models.CharField(max_length=100,db_column="nameUser")
    fk_Rol = models.ForeignKey(Rol,default=1,on_delete=models.CASCADE,db_column="fk_Rol")
    fk_Gender = models.ForeignKey(Gender,default=1,on_delete=models.CASCADE,db_column="fk_Gender")
    class Meta:
        db_table = "users"

class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True,db_column="idProduct")
    nameProduct = models.CharField(max_length=100,db_column="nameProduct")
    priceProduct = models.FloatField(default=0,db_column="priceProduct")
    class Meta:
        db_table = "products"