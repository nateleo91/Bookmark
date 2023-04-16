from models import Bookmark

def add_bookmark():
    title = input("Enter the title: ")
    url = input("Enter the URL: ")

    bookmark = Bookmark(title=title, url=url)
    bookmark.save()

    print("Bookmark saved.")

def list_bookmarks():
    for bookmark in Bookmark.select():
        print(f"{bookmark.title}: {bookmark.url}")

def delete_bookmark():
    title = input("Enter the title of the bookmark to delete: ")

    bookmark = Bookmark.get(Bookmark.title == title)
    bookmark.delete_instance()

    print("Bookmark deleted.")

def search_bookmarks():
    query = input("Enter the search query: ")

    bookmarks = Bookmark.select().where(Bookmark.title.contains(query) | Bookmark.url.contains(query))

    for bookmark in bookmarks:
        print(f"{bookmark.title}: {bookmark.url}")

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
