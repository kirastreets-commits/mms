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

    # ----------------------------
    # IF PLAYER EXISTS → RETURN
    # ----------------------------
    if player is not None:

        # 🔧 patch missing fields safely
        if not hasattr(player, "has_starter"):
            player.has_starter = False
            save_player(player)  # persist fix to disk

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
    
    print(f"Loading player {user_id}")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT data FROM players WHERE user_id = %s",
        (str(user_id),)
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result is None:
        return None

    data = result[0]

    return Player.from_dict(data, Creature)
