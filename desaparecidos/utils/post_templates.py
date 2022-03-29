from desaparecidos.handlers import directory_handler as dir


def thread_title(location):
    return "URGENTE: DESAPARECIDO en " + location.upper()


def thread_body(missing_person_id):
    return \
        "[CENTER]" + \
        "[URL=" + dir.URL_MISSING_PERSON_PROFILE + missing_person_id + "/]" + \
        "[IMG]" + dir.URL_MISSING_PERSON_IMAGE + missing_person_id + ".jpg" + "[/IMG]" + \
        '\n' + \
        '\n' + \
        "[SIZE=7][B] CONTACTO + INFORMACIÓN [/B][/SIZE][/URL]" + \
        '\n' + \
        '\n' + \
        "[SIZE=6][B] Muchas gracias por la colaboración [/B][/SIZE][/CENTER]"


def bump_message():
    return "Up!"


def status_update_message(status):
    return "[SIZE=6][B]" + status.capitalize() + "[/B][/SIZE]"
