catalog = {}
borrowed_books = []
members = set()

def add_book(book_id, title, author, year):
    catalog[book_id] = (title, author, year)

def borrow_book(book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book Borrowed")
    else:
        print("Book not available")

def return_book(book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book Returned")

def register_member(member):
    members.add(member)

def show_available():
    print("\nAvailable Books:")
    for book_id in catalog:
        if book_id not in borrowed_books:
            print(book_id, catalog[book_id])

# Demo
add_book(1,"Python","Guido",2020)
add_book(2,"Java","James",2019)
add_book(3,"C++","Bjarne",2018)
add_book(4,"AI","Andrew",2023)

register_member(101)
register_member(102)
register_member(103)
register_member(103)

borrow_book(1)
borrow_book(2)

return_book(1)

show_available()
