import itertools
import string
import random

from teams.models import Team
from legacy_teams.models import Team as LegacyTeam

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
        team = Team(
            name=_random_str(string.ascii_uppercase, 12),
            tv_name=tv_name,
            city=random.choice(CITIES),
        )
        team.save()
        created += 1
        if created % 10000 == 0:
            print(f"Created {created} teams...")
    print("Finished creating teams")

def create_legacy_teams():
    created = 0
    for team in Team.objects.all():
        legacy_team = LegacyTeam(
            name=team.name,
            tv_name=team.tv_name,
            city=team.city,
        )
        legacy_team.save()
        created += 1
        if created % 10000 == 0:
            print(f"Created {created} teams...")
    print("Finished creating teams")

def clear():
    Team.objects.all().delete()
    LegacyTeam.objects.all().delete()

def run():
    create_teams()

def run_legacy():
    create_legacy_teams()