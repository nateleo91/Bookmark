import peewee
import pyperclip
import argparse
import sys

db = peewee.SqliteDatabase('bookmarks.db')

class Bookmark(peewee.Model):
    url = peewee.CharField(unique=True)
    description = peewee.CharField()

    class Meta:
        database = db

parser = argparse.ArgumentParser(description='Bookmark URLs from the command line')
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add', help='Add a new bookmark')
add_parser.add_argument('url', help='URL to bookmark')
add_parser.add_argument('-d', '--description', help='Description of the bookmark')

list_parser = subparsers.add_parser('list', help='List all bookmarks')

delete_parser = subparsers.add_parser('delete', help='Delete a bookmark')
delete_parser.add_argument('url', help='URL to delete')

def add_bookmark(url, description):
    try:
        bookmark = Bookmark.create(url=url, description=description)
        bookmark.save()
        print(f'Added bookmark: {url}')
    except peewee.IntegrityError:
        print(f'Bookmark already exists: {url}')

def list_bookmarks():
    bookmarks = Bookmark.select()
    for bookmark in bookmarks:
        print(f'{bookmark.url} - {bookmark.description}')

def delete_bookmark(url):
    bookmark = Bookmark.get_or_none(url=url)
    if bookmark is not None:
        bookmark.delete_instance()
        print(f'Deleted bookmark: {url}')
    else:
        print(f'Bookmark not found: {url}')

def main(args):
    db.connect()
    db.create_tables([Bookmark])

    while True:
        print('Please choose an option:')
        print('1. View list')
        print('2. Add bookmark')
        print('3. Edit bookmark')
        print('4. Delete bookmark')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            list_bookmarks()
        elif choice == '2':
            url = input('Enter the URL to bookmark: ')
            description = input('Enter a description for the bookmark: ')
            add_bookmark(url, description)
        elif choice == '3':
            url = input('Enter the URL of the bookmark to edit: ')
            description = input('Enter the new description for the bookmark: ')
            edit_bookmark(url, description)
        elif choice == '4':
            url = input('Enter the URL of the bookmark to delete: ')
            delete_bookmark(url)
        elif choice == '5':
            break
        else:
            print('Invalid choice')

    db.close()

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)