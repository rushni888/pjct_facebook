from django.db import models
import datetime

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



class ProfilePic(models.Model):
    pic=models.FileField(upload_to='profilepicture/')
    fk_user=models.ForeignKey(LoginDummy,on_delete=models.CASCADE)

class FileUpload(models.Model):
    name=models.CharField(max_length=200)
    pic=models.FileField(upload_to='files/')





# class Friends(models.Model):
#     sender=models.ForeignKey(LoginDummy,on_delete=models.CASCADE)
#     reciever=models.ForeignKey(LoginDummy,on_delete=models.CASCADE)
#     status=models.BooleanField(default=False)
# dob=models.DateField(default=datetime.date.today)




