import itertools
import string
import random

from teams.models import Team

CITIES = [
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

def _random_str(alphabet, size):
    return "".join(random.choice(alphabet) for _ in range(size))

def _generate_tv_names_combinations():
    for subset in itertools.product(string.ascii_uppercase, repeat=4):
        yield "".join(subset)

def create_teams():
    created = 0
    for tv_name in _generate_tv_names_combinations():
        name = _random_str(string.ascii_uppercase, 12)
        city = random.choice(CITIES)
        team = Team(
            name=name,
            name_with_index=name,
            tv_name=tv_name,
            tv_name_without_unique=tv_name,
            city=city,
            city_with_partial_index=city,
        )
        team.save()
        created += 1
        if created % 10000 == 0:
            print(f"Created {created} teams...")
    print("Finished creating teams")

def clear():
    Team.objects.all().delete()

def run():
    create_teams()