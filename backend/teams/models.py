from django.db import models

PLAYER_POSITION_CHOICES = [
    ('GK', 'Goalkeeper'),
    ('RB', 'Right back'),
    ('CB', 'Center back'),
    ('LB', 'Left back'),
    ('DM', 'Defensive midfielder'),
    ('CM', 'Central midfielder'),
    ('AM', 'Attacking midfielder'),
    ('CF', 'Center forward'),
    ('RW', 'Right winger'),
    ('LW', 'Left winger'),
]

class City(models.Model):
    name = models.CharField(max_length=255)

class Team(models.Model):
    name = models.CharField(max_length=255)
    tv_name = models.CharField(max_length=3)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tv_name'],
                name='%(app_label)s_%(class)s_tv_name_unique',
            ),
        ]

class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=PLAYER_POSITION_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
