import random

LOVE_MESSAGES = [
    "{name} rushes off with the gift and proudly displays it in its shelter.",
    "{name} carefully places the gift in its favourite corner.",
    "{name} seems delighted and immediately rearranges its shelter around the gift."
]

LIKE_MESSAGES = [
    "{name} carries the gift back to its shelter.",
    "{name} happily adds the gift to its collection.",
    "{name} finds a comfortable place for the gift."
]

NEUTRAL_MESSAGES = [
    "{name} accepts the gift and places it in its shelter.",
    "{name} quietly adds the gift to its belongings.",
    "{name} finds a place for the gift, though it doesn't seem particularly excited."
]

DISLIKE_MESSAGES = [
    "{name} nudges the gift back toward you.",
    "{name} doesn't seem interested in keeping the gift.",
    "{name} refuses to place the gift in its shelter."
]

FAVORITE_MESSAGES = [
    "{name} immediately places the gift in a special spot inside its shelter.",
    "{name} treasures the gift and proudly displays it.",
    "{name} seems absolutely delighted and makes the gift a centerpiece of its shelter."
]

def get_gift_message(creature, result):
    pool_map = {
        "loves": LOVE_MESSAGES,
        "likes": LIKE_MESSAGES,
        "neutral": NEUTRAL_MESSAGES,
        "dislikes": DISLIKE_MESSAGES
    }

    pool = pool_map.get(result["reaction"], NEUTRAL_MESSAGES)

    return random.choice(pool).format(name=creature.name)
