from handlers import directory_handler as dir
from handlers import database_handler as db
from handlers import forum_handler as fc
from utils import post_templates as pt
from utils import time_operations as to

from datetime import datetime
import time


def check_directory():
    missing_persons_ids = dir.get_all_missing_persons_ids()

    for person_id in missing_persons_ids:
        if not db.missing_person_exists(person_id):
            missing_since, location, status = dir.get_missing_person_data(person_id)
            db.create_missing_person(person_id, missing_since, location, status)

            if status == 'DESAPARECIDO':
                post_id = create_missing_person_thread(person_id, location)
                db.update_missing_person_thread_id(person_id, post_id)
                db.update_missing_person_last_bump(person_id, datetime.now())
                time.sleep(30)


def check_monitored_persons():
    monitored_persons = db.get_monitored_persons()

    for person in monitored_persons:
        person_id, missing_since, location, status, last_bump, thread_id = person
        _, _, current_status = dir.get_missing_person_data(person_id)

        if current_status == 'DESAPARECIDO':
            bump_period = to.get_bump_period(missing_since)
            time_since_last_bump = to.hour_difference(last_bump)
            if time_since_last_bump >= bump_period:
                db.update_missing_person_last_bump(person_id, datetime.now())
                fc.reply_to_thread(thread_id, pt.bump_message())
                time.sleep(30)

        else:
            db.update_missing_person_status(person_id, current_status)
            fc.reply_to_thread(thread_id, pt.status_update_message(current_status))
            time.sleep(30)


def create_missing_person_thread(person_id, location):
    return fc.create_thread(pt.thread_title(location), pt.thread_body(person_id))
