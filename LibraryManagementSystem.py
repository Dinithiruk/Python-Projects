
class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} by {self.author} has been checked in.")
        else:
            print(f"{self.title} by {self.author} is already checked in.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")
        print(f"Status: {'Checked out' if self.checked_out else 'Available'}")

#-- Book class --
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

#-- Member class --
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.checked_out_books = []

    def check_out_book(self, book):
        if not book.checked_out:
            book.check_out()
            self.checked_out_books.append(book)
            print(f"{self.name} has checked out '{book.title}'")
        else:
            print(f"{book.title} is already checked out.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.check_in()
            self.checked_out_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} hasn't checked out '{book.title}'")

    def display_checked_out_books(self):
        if self.checked_out_books:
            print(f"{self.name}'s Checked Out Books:")
            for book in self.checked_out_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no books checked out.")


# Instances of the books
book1=Book("b001","Harry Potter","Rodny way","Classic")
book2=Book("b002","The Great Gatsby","F. Scott Fitzgerald","Classic")
book3=Book("b003","To Kill a Mockingbird","Harper Lee","Fiction")

# Instances of the members
member1= LibraryMember("John",201)
member2= LibraryMember("Tom",202)
member3= LibraryMember("Peter",203)

print("\n---- Book Information ---- ")
book1.display_info()
book2.display_info()
book3.display_info()

print("\n")
member1.check_out_book(book1)
member2.check_out_book(book1)
member3.check_out_book(book2)

print("\n")
member1.display_checked_out_books()
member2.display_checked_out_books()
member3.display_checked_out_books()


print("\n")
member1.return_book(book1)
member1.display_checked_out_books()

