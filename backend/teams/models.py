from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    name_with_index = models.CharField(max_length=255, db_index=True)

    tv_name = models.CharField(max_length=4, unique=True)
    tv_name_without_unique = models.CharField(max_length=4)

    city = models.CharField(max_length=255)
    city_with_partial_index = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tv_name_without_unique'],
                name='%(app_label)s_%(class)s_tv_name_unique',
            ),
        ]
        indexes = [
            models.Index(
                fields=['city_with_partial_index'],
                condition=models.Q(city_with_partial_index="Zora's Domain"),
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
