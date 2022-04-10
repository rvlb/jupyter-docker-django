from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    tv_name = models.CharField(max_length=4)
    city = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tv_name'],
                name='%(app_label)s_%(class)s_tv_name_unique',
            ),
        ]
        indexes = [
            models.Index(
                fields=['city'],
                condition=models.Q(city="Zora's Domain"),
                name='%(app_label)s_%(class)s_city_zora',
            ),
        ]

class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    teams = models.ManyToManyField(Team)
