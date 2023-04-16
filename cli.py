from models import Bookmark
from prettytable import PrettyTable

def add_bookmark():
    name = input("Enter the name: ")
    url = input("Enter the URL: ")

    bookmark = Bookmark(name=name, url=url)
    bookmark.save()

    print("Bookmark saved.")

def list_bookmarks():
    bookmarks = Bookmark.select()
    if bookmarks.exists():
        table = PrettyTable(['Name', 'URL'])
        for bookmark in bookmarks:
            table.add_row([bookmark.name, bookmark.url])
        print(table)
    else:
        print('No bookmarks found.')


def delete_bookmark():
    name = input("Enter the name of the bookmark to delete: ")

    bookmark = Bookmark.get(Bookmark.name == name)
    bookmark.delete_instance()

    print("Bookmark deleted.")

def search_bookmarks():
    query = input("Enter the search query: ")

    bookmarks = Bookmark.select().where(Bookmark.name.contains(query))

    for bookmark in bookmarks:
        print(f"{bookmark.name}: {bookmark.url}")

if __name__ == '__main__':
    while True:
        print("Enter the number of the action you want to perform:")
        print("1. Add a bookmark")
        print("2. List all bookmarks")
        print("3. Delete a bookmark")
        print("4. Search bookmarks")
        print("5. Quit")

        choice = input("> ")

        if choice == '1':
            add_bookmark()
        elif choice == '2':
            list_bookmarks()
        elif choice == '3':
            delete_bookmark()
        elif choice == '4':
            search_bookmarks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
