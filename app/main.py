import datetime
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    for friend in friends:
        if (
                not friend.get("vaccine")
                or friend.get("vaccine").get("expiration_date")
                < datetime.date.today()
        ):
            return "All friends should be vaccinated"

    count = 0
    for friend in friends:
        if not friend.get("wearing_a_mask"):
            count += 1
    if count > 0:
        return f"Friends should buy {count} masks"

    return f"Friends can go to {cafe.name}"
