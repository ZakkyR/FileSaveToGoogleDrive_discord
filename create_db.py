"""
DB作成
"""

import sys
import sqlite3


def create_database():
    # db作成
    db = sqlite3.connect('db.sqlite3')

    cur = db.cursor()

    try:
        sql = """
                CREATE TABLE PARAM(
                    CD TEXT NOT NULL PRIMARY KEY,
                    VALUE TEXT NOT NULL,
                    NOTE TEXT,
                    CREATE_DATETIME TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime'))
                )"""
        cur.execute(sql)

        sql = """
                CREATE TABLE SERVER(
                    ID INTEGER NOT NULL PRIMARY KEY,
                    SERVER_ID TEXT NOT NULL,
                    FOLDER_NAME TEXT NOT NULL,
                    SHOW_MESSAGE INTEGER NOT NULL,
                    NOTE TEXT,
                    CREATE_DATETIME TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
                    UNIQUE(ID, SERVER_ID)
                )"""
        cur.execute(sql)

        sql = """
                CREATE TABLE CHANNEL(
                    ID INTEGER NOT NULL PRIMARY KEY,
                    SERVER_ID TEXT NOT NULL,
                    CHANNEL_ID TEXT NOT NULL,
                    FOLDER_NAME TEXT NOT NULL,
                    NOTE TEXT
                    CREATE_DATETIME TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
                    UNIQUE(ID, SERVER_ID, CHANNEL_ID)
                )"""
        cur.execute(sql)

        db.commit()
        db.close()

        print('Table created.')

    except sqlite3.Error as e:
        print('sqlite3.Error occurred:{}'.format(e.args[0]), file=sys.stderr)


if __name__ == '__main__':
    create_database()
