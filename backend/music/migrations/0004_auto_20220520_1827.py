# Generated by Django 3.2.12 on 2022-05-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20220404_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, choices=[('pop_music', 'Pop Music'), ('rock', 'Rock'), ('rythm_and_blues', 'Rhythm and Blues'), ('classical_music', 'Classical Music'), ('hip_hop_music', 'Hip Hop Music'), ('country_music', 'Country Music'), ('jazz', 'Jazz'), ('folk_music', 'Folk Music'), ('electronic_music', 'Electronic Music'), ('soul_music', 'Soul Music'), ('heavy_metal', 'Heavy Metal'), ('progressive_rock', 'Progressive Rock'), ('alternative_rock', 'Alternative Rock'), ('indie_rock', 'Indie Rock'), ('punk_rock', 'Punk Rock'), ('pop_rock', 'Pop Rock'), ('funk', 'Funk'), ('techno', 'Techno'), ('reggae', 'Reggae'), ('rap', 'Rap'), ('grunge', 'Grunge')], max_length=200),
        ),
        migrations.AddField(
            model_name='song',
            name='release_date',
            field=models.DateTimeField(null=True),
        ),
    ]
