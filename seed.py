from peewee import *
import os

db = SqliteDatabase('bookmarks.db')

class Bookmark(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    url = CharField()
    ip_address = CharField()

    class Meta:
        database = db

if __name__ == '__main__':
    # Create the database file if it doesn't exist
    if not os.path.exists('bookmarks.db'):
        open('bookmarks.db', 'w').close()

    # Connect to the database and create the tables
    db.connect()
    db.create_tables([Bookmark])

    # Insert some sample data
    Bookmark.create(name='Google', url='https://www.google.com/', ip_address='8.8.8.8')
    Bookmark.create(name='Facebook', url='https://www.facebook.com/', ip_address='69.63.176.13')
