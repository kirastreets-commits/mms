import json

from models.player import Player
from models.creature import Creature
from data.preserves import PRESERVES

from systems.database import get_connection
from data.species import SPECIES_REGISTRY


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
    print("💾 SAVING STATE SNAPSHOT")
    print("CREATURE COUNT:", len(player.creatures))
    print("INVENTORY:", player.inventory)
    print("CALLER:", __import__("traceback").format_stack()[-3])


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


    # ----------------------------
    # 🌿 PRESERVE MIGRATION PATCH
    # ----------------------------
    # Fixes old saves created before preserves existed

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


    # ----------------------------
    # 💾 SAVE MIGRATED DATA
    # ----------------------------
    # Updates old database entries automatically

    save_player(player)


    return player

def update_sanctuary_homes(player):
    """
    Adds sanctuary homes to existing sanctuary-native creatures.
    Only affects creatures missing a sanctuary location.
    """

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

        # Make sure shelter exists
        if not hasattr(creature, "shelter") or creature.shelter is None:
            creature.shelter = {}

        # Only assign if they don't already have a home
        if not creature.shelter.get("location"):

            creature.shelter["location"] = home["location"]
            creature.shelter["site"] = home["name"]
            creature.shelter["type"] = home["shelter"]

            updated = True

    return updated
