import json

from models.player import Player
from models.creature import Creature
from systems.database import get_connection

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
    # CREATE NEW PLAYER
    # ----------------------------
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

    return Player.from_dict(data, Creature)
