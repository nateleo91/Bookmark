from peewee import *

db = SqliteDatabase('bookmarks.db')

class Bookmark(Model):
    title = CharField()
    url = CharField()

    class Meta:
        database = db

# create the bookmarks table using SQL
db.execute_sql('''
    CREATE TABLE IF NOT EXISTS bookmarks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT
    );
''')
