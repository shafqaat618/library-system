
books = [
    {"id": 1, "title": "Python Basics", "author": "John Smith"},
    {"id": 2, "title": "Database Systems", "author": "Thomas Connolly"},
    {"id": 3, "title": "Data Science", "author": "Joel Grus"},
    {"id": 4, "title": "Computer Networks", "author": "Andrew Tanenbaum"},
    {"id": 5, "title": "Clean Code", "author": "Robert Martin"}
]

def display_books():
    print("Library Book Catalog")
    print("--------------------")
    for book in books:
        print(f"{book['id']}. {book['title']} - {book['author']}")

if __name__ == "__main__":
    display_books()

def search_book(keyword):
    found = False

    for book in books:
        if keyword.lower() in book["title"].lower():
            print(f"{book['title']} - {book['author']}")
            found = True

    if not found:
        print("No book found.")
