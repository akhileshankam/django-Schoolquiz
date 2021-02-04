from django.db import models

# Create your models here.
class score1(models.Model):
    score1=models.IntegerField(default=1)
    username=models.CharField(max_length=50,default=1,primary_key=True)
    def __str__(self):
        return self.username
class score2(models.Model):
    score2=models.IntegerField(default=1)
    username=models.CharField(max_length=50,default=1,primary_key=True)
    def __str__(self):
        return self.username
class quiz1(models.Model):
    username=models.CharField(max_length=50,default=1)
    answer=models.CharField(max_length=50,default=1)

    def __str__(self):
        return self.username
class quiz2(models.Model):
    username=models.CharField(max_length=50,default=1)
    answer=models.CharField(max_length=50,default=1)

    def __str__(self):
        return self.username