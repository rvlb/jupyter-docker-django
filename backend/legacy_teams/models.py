from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    tv_name = models.CharField(max_length=4, unique=True)
    city = models.CharField(max_length=255)

class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    teams = models.ManyToManyField(Team)
