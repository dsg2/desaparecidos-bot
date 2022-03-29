from datetime import datetime


def hour_difference(last_bump):
    duration = datetime.now() - datetime.fromisoformat(last_bump)
    duration_in_seconds = duration.total_seconds()
    return divmod(duration_in_seconds, 3600)[0]


def day_difference(d1, d2):
    return abs((d2 - d1).days)


def get_bump_period(missing_since):
    days_missing = day_difference(datetime.today(), datetime.fromisoformat(missing_since))
    weeks_missing = int(days_missing / 7)
    return pow(2, weeks_missing)
