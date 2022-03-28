import sqlite3
import os

DATABASE_PATH = "../database/"


def open_connection():
    if not os.path.exists(DATABASE_PATH):
        os.makedirs(DATABASE_PATH)

    connection = sqlite3.connect(DATABASE_PATH + 'missing_persons.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS missing_persons (
                        missing_person_id TEXT PRIMARY KEY,
                        missing_since DATE,
                        location STRING,
                        status STRING,
                        last_bump DATE,
                        thread_id STRING
                    );""")
    connection.commit()
    return connection


def create_missing_person(missing_person_id, missing_since, location, status, last_bump=None, thread_id=None):
    cursor.execute("INSERT INTO missing_persons values(?,?,?,?,?,?)",
                   (missing_person_id, missing_since, location, status, last_bump, thread_id))
    connection.commit()


def get_missing_person(missing_person_id):
    cursor.execute("SELECT * FROM missing_persons WHERE missing_person_id = (?)", (missing_person_id, ))
    return cursor.fetchall()


def missing_person_exists(missing_person_id):
    cursor.execute("SELECT EXISTS(SELECT 1 FROM missing_persons WHERE missing_person_id=(?) LIMIT 1)",
                   (missing_person_id,))
    return bool(cursor.fetchall()[0][0])


def update_missing_person_thread_id(missing_person_id, thread_id):
    cursor.execute("UPDATE missing_persons SET thread_id = (?) WHERE missing_person_id = (?)",
                   (thread_id, missing_person_id))
    connection.commit()


def update_missing_person_status(missing_person_id, status):
    cursor.execute("UPDATE missing_persons SET status = (?) WHERE missing_person_id = (?)",
                   (status, missing_person_id))
    connection.commit()


def update_missing_person_last_bump(missing_person_id, last_bump):
    cursor.execute("UPDATE missing_persons SET last_bump = (?) WHERE missing_person_id = (?)",
                   (last_bump, missing_person_id))
    connection.commit()


def get_monitored_persons():
    cursor.execute('SELECT * FROM missing_persons WHERE thread_id IS NOT NULL AND status = "DESAPARECIDO"')
    return cursor.fetchall()


connection = open_connection()
cursor = connection.cursor()
