from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    topic_name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)


class user(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)


    def __str__(self):
        return self.first_name