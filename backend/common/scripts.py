import itertools
import string
import random

from teams.models import Team, City
from legacy_teams.models import Team as LegacyTeam, City as LegacyCity

def _random_str(alphabet, size):
    return "".join(random.choice(alphabet) for _ in range(size))

def create_cities(legacy=False):
    model = City
    if legacy:
        model = LegacyCity
    cities = [
        "Kakariko Village",
        "Tarrey Town",
        "Gerudo Town",
        "Lurelin Village",
        "Rito Village",
        "Goron City",
        "Zora's Domain",
        "Korok Forest",
        "Hyrule Castle Town",
        "Hateno Village",
    ]
    for city_name in cities:
        city = model(
            name=city_name
        )
        city.save()
    print("Finished creating cities")

def _generate_tv_names_combinations():
    for subset in itertools.product(string.ascii_uppercase, repeat=4):
        yield "".join(subset)

def create_teams(legacy=False):
    team_model = Team
    city_model = City
    if legacy:
        team_model = LegacyTeam
        city_model = LegacyCity
    cities_ids = city_model.objects.all().values_list("id", flat=True)
    created = 0
    for tv_name in _generate_tv_names_combinations():
        city = city_model.objects.get(id=random.choice(cities_ids))
        name = _random_str(string.ascii_uppercase, 12)
        team = team_model(
            name=name,
            tv_name=tv_name,
            city=city,
        )
        team.save()
        created += 1
        if created % 10000 == 0:
            print(f"Created {created} teams...")
    print("Finished creating teams")

def clear():
    Team.objects.all().delete()
    LegacyTeam.objects.all().delete()
    City.objects.all().delete()
    LegacyCity.objects.all().delete()

def run():
    create_cities()
    create_teams()

def run_legacy():
    create_cities(legacy=True)
    create_teams(legacy=True)