from peewee import *

db = SqliteDatabase('bookmarks.db')

class Bookmark(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    url = CharField()
    ip_address = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Bookmark])

import argparse

parser = argparse.ArgumentParser(description='Bookmark Manager')

subparsers = parser.add_subparsers(dest='command', help='Available commands')

add_parser = subparsers.add_parser('add', help='Add a new bookmark')
add_parser.add_argument('name', help='Bookmark name')
add_parser.add_argument('url', help='Bookmark URL')
add_parser.add_argument('--ip', help='Bookmark IP address')

args = parser.parse_args()

if args.command == 'add':
    bookmark = Bookmark(name=args.name, url=args.url, ip_address=args.ip)
    bookmark.save()
    print('Bookmark added successfully!')

