import sqlite3
from data_controller import *

def create_table():
    conn = sqlite3.connect('testdb2.sqlite')

    cursor = conn.cursor()

    query =     '''
	    CREATE TABLE IF NOT EXISTS user(
	    	id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT,
	        phone TEXT
	    )
	'''

    cursor.execute(query)

    conn.commit()
    conn.close()


def add_user(roll, name, phone):
    conn = sqlite3.connect('testdb2.sqlite')

    cursor = conn.cursor()

    query = '''
	    INSERT INTO user( roll, name, phone )
	    	        VALUES ( ?,?,? )
	'''

    cursor.execute(query, (roll, name, phone))

    conn.commit()
    conn.close()


def get_user():
    conn = sqlite3.connect('testdb2.sqlite')

    cursor = conn.cursor()

    query = '''
	    SELECT roll, name, phone
	    FROM user
	'''

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


def get_user_by_roll(roll):
    conn = sqlite3.connect('testdb2.sqlite')

    cursor = conn.cursor()

    query = '''
	    SELECT roll, name, phone
	    FROM user
	    WHERE roll = {}
	'''.format(roll)

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


def update_user(roll, name, phone):
    conn = sqlite3.connect('testdb2.sqlite')

    cursor = conn.cursor()

    query = '''
	    UPDATE user
	    SET name = ?, phone = ?
	    WHERE roll = ?
	'''

    cursor.execute(query, (name, phone, roll))

    conn.commit()
    conn.close()


def delete_user(roll):
    conn = sqlite3.connect('testdb2.sqlite')

    cursor = conn.cursor()

    query = '''
	    DELETE
	    FROM user
	    WHERE roll = {}
	'''.format(roll)

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows