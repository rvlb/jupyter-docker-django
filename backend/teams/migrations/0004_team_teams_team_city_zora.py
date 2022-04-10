# Generated by Django 3.2.12 on 2022-04-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_team_name'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='team',
            index=models.Index(condition=models.Q(('city', "Zora's Domain")), fields=['city'], name='teams_team_city_zora'),
        ),
    ]
