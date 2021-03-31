from django.db import models

# Create your models here.
# class Destination:
#     id:int
#     name:str
#     img:str
#     desc:str
#     price:int
# class Product:
#     id : int
#     name : str
#     desc: str
#     price: float
#     img : str

# class Login(models.Model):
#     username=models.CharField(max_length=260)
#     password=models.CharField(max_length=20)

class LoginDummy(models.Model):
    user=models.CharField(max_length=260)
    pwd=models.CharField(max_length=50)


class UserDetails(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=50)
    user_id=models.ForeignKey(LoginDummy,on_delete=models.CASCADE)



