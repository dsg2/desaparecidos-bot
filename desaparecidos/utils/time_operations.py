from datetime import datetime
from random import randint

GLOBAL_BUMP_DELAY = 5

time_offset = randint(-5, 5)


def day_difference(d1, d2):
    return abs((d2 - d1).days)


def hour_difference(last_bump):
    duration = datetime.now() - datetime.fromisoformat(last_bump)
    duration_in_seconds = duration.total_seconds()
    return divmod(duration_in_seconds, 3600)[0]


def minute_difference(last_bump):
    duration = datetime.now() - datetime.fromisoformat(last_bump)
    duration_in_seconds = duration.total_seconds()
    return divmod(duration_in_seconds, 60)[0]


def get_weeks_missing(missing_since):
    days_missing = day_difference(datetime.today(), datetime.fromisoformat(missing_since))
    weeks_missing = int(days_missing / 7) + 1
    return weeks_missing


def get_bump_period(weeks_missing):
    return weeks_missing * 60 + time_offset


def generate_new_time_offset():
    global time_offset
    time_offset = randint(-5, 5)
