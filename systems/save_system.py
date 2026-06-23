import json
import os

from models.player import Player
from models.creature import Creature

SAVE_FOLDER = "data/saves/players"


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

    os.makedirs(SAVE_FOLDER, exist_ok=True)

    file_path = os.path.join(SAVE_FOLDER, f"{player.user_id}.json")
    tmp_path = file_path + ".tmp"

    # safety: ensure data is serialisable
    data = player.to_dict()

    with open(tmp_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    # atomic replace (prevents corrupted saves)
    os.replace(tmp_path, file_path)


# ----------------------------
# LOAD PLAYER
# ----------------------------
def load_player(user_id):

    file_path = os.path.join(SAVE_FOLDER, f"{str(user_id)}.json")

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    player = Player.from_dict(data, Creature)

    # safety check (prevents broken data types slipping through)
    if not isinstance(player.inventory, dict):
        player.inventory = {}

    if not isinstance(player.discovered_species, list):
        player.discovered_species = []

    return player
