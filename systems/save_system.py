import json

from models.player import Player
from models.creature import Creature

from data.preserves import PRESERVES
from data.species import SPECIES_REGISTRY

from systems.database import get_connection


# ----------------------------
# PLAYER MIGRATIONS
# ----------------------------

def update_sanctuary_homes(player):

    updated = False

    for creature in player.creatures:

        species_data = SPECIES_REGISTRY.get(
            creature.species,
            {}
        )

        if not species_data.get("sanctuary_native"):
            continue

        home = species_data.get("sanctuary_home")

        if not home:
            continue

        if not hasattr(creature, "shelter") or creature.shelter is None:
            creature.shelter = {}

        if not creature.shelter.get("location"):

            creature.shelter["location"] = home["location"]
            creature.shelter["site"] = home["name"]
            creature.shelter["type"] = home["shelter"]

            updated = True

    return updated



def update_preserves(player):

    updated = False

    if not hasattr(player, "preserves") or player.preserves is None:

        player.preserves = {
            preserve_id: {
                "level": 1,
                "restoration": 0,
                "unlocked": PRESERVES[preserve_id].get(
                    "unlock_level",
                    1
                ) == 1
            }
            for preserve_id in PRESERVES
        }

        updated = True

    return updated



def migrate_player(player):

    updated = False

    if update_sanctuary_homes(player):
        updated = True

    if update_preserves(player):
        updated = True

    return updated



# ----------------------------
# CREATE OR LOAD PLAYER
# ----------------------------

def get_or_create_player(user):

    user_id = str(user.id)

    player = load_player(user_id)

    if player is None:

        player = Player(
            user_id=user_id,
            name=user.name,
            has_starter=False
        )

        save_player(player)

    return player



# ----------------------------
# SAVE PLAYER
# ----------------------------

def save_player(player):

    print(f"Saving player {player.user_id}")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO players (user_id, data)
        VALUES (%s, %s)
        ON CONFLICT (user_id)
        DO UPDATE SET data = EXCLUDED.data
    """, (
        str(player.user_id),
        json.dumps(player.to_dict())
    ))

    conn.commit()

    cur.close()
    conn.close()



# ----------------------------
# LOAD PLAYER
# ----------------------------

def load_player(user_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT data FROM players WHERE user_id = %s",
        (str(user_id),)
    )

    result = cur.fetchone()

    cur.close()
    conn.close()


    if not result or not result[0]:
        return None


    data = result[0]

    if isinstance(data, str):
        data = json.loads(data)


    player = Player.from_dict(
        data,
        Creature
    )


    # Run save upgrades here
    if migrate_player(player):
        save_player(player)


    return player
