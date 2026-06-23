import json
import os

from models.player import Player
from models.creature import Creature


SAVE_FOLDER = "data/saves/players"


# ----------------------------
# CREATE OR LOAD PLAYER
# ----------------------------

def get_or_create_player(user):

    player = load_player(user.id)

    # ----------------------------
    # IF PLAYER EXISTS → RETURN
    # ----------------------------

    if player:
        if not hasattr(player, "has_starter"):
            player.has_starter = False
        return player

    # ----------------------------
    # CREATE NEW PLAYER
    # ----------------------------

    player = Player(
        user_id=str(user.id),
        name=user.name,
        has_starter=False
    )

    save_player(player)

    return player


# ----------------------------
# SAVE PLAYER
# ----------------------------

def save_player(player):

    os.makedirs(SAVE_FOLDER, exist_ok=True)

    file_path = f"{SAVE_FOLDER}/{player.user_id}.json"

    with open(file_path, "w") as file:
        json.dump(player.to_dict(), file, indent=4)


# ----------------------------
# LOAD PLAYER
# ----------------------------

def load_player(user_id):

    file_path = f"{SAVE_FOLDER}/{user_id}.json"

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as file:
        data = json.load(file)

    return Player.from_dict(data, Creature)