from datetime import datetime

INDIVIDUAL_BUMP_DELAY = 60
GLOBAL_BUMP_DELAY = 5


def day_difference(d1, d2):
    return abs((d2 - d1).days)


def minutes_since(last_bump):
    duration = datetime.now() - datetime.fromisoformat(last_bump)
    duration_in_seconds = duration.total_seconds()
    return divmod(duration_in_seconds, 60)[0]
