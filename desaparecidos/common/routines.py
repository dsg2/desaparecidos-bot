from desaparecidos.handlers import directory_handler as dir
from desaparecidos.handlers import database_handler as db
from desaparecidos.handlers import forum_handler as fc
from desaparecidos.utils import post_templates as pt
from desaparecidos.utils import time_operations as to
from desaparecidos.utils import string_parser as parser

from datetime import datetime
import time


def check_directory(post_mode):
    missing_persons_ids = dir.get_all_missing_persons_ids()

    for person_id in missing_persons_ids:
        if not db.missing_person_exists(person_id):
            missing_since, location, status = dir.get_missing_person_data(person_id)
            db.create_missing_person(person_id, missing_since, location, status)
            today = datetime.today().date()

            if post_mode and status == 'DESAPARECIDO' and \
               to.day_difference(today, missing_since) <= 30:

                post_id = create_missing_person_thread(person_id, location)
                db.update_missing_person_thread_id(person_id, post_id)
                db.update_missing_person_last_bump(person_id, datetime.now())
                time.sleep(30)


def check_monitored_persons():
    monitored_persons = db.get_monitored_persons()

    for person in monitored_persons:
        person_id, missing_since, location, status, last_bump, thread_id = person
        _, _, current_status = dir.get_missing_person_data(person_id)
        last_global_bump = db.get_last_global_bump()

        if current_status == 'DESAPARECIDO':
            time_since_last_bump = to.minutes_since(last_bump)
            time_since_last_global_bump = to.minutes_since(last_global_bump)

            if time_since_last_bump >= to.INDIVIDUAL_BUMP_DELAY and \
               time_since_last_global_bump >= to.GLOBAL_BUMP_DELAY:

                fc.reply_to_thread(thread_id, pt.bump_message())
                db.update_missing_person_last_bump(person_id, datetime.now())
                time.sleep(30)

        else:
            fc.reply_to_thread(thread_id, pt.status_update_message(current_status, fc.get_collaborators(thread_id)))
            db.update_missing_person_status(person_id, current_status)
            time.sleep(30)


def create_missing_person_thread(person_id, location):
    return fc.create_thread(pt.thread_title(parser.remove_location_redundancy(location)), pt.thread_body(person_id))
