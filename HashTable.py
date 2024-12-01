class LibraryHashTable:
    def __init__(self):
        self.books_by_title = {}
        self.books_by_author = {}

    def add_book(self, title, authors, genre, publication_year, isbn=None, copies=1):
        book = {
            "title": title,
            "authors": authors,
            "genre": genre,
            "publication_year": publication_year,
            "isbn": isbn,
            "copies": copies,
        }

        self.books_by_title[title.lower()] = book

        for author in authors:
            author_key = author.lower()
            if author_key not in self.books_by_author:
                self.books_by_author[author_key] = []
            self.books_by_author[author_key].append(book)

        print(f"Book '{title}' added successfully.")

    def search_by_title(self, title):
        title_key = title.lower()
        if title_key in self.books_by_title:
            return self.books_by_title[title_key]
        else:
            return None

    def search_by_author(self, author):
        author_key = author.lower()
        if author_key in self.books_by_author:
            return self.books_by_author[author_key]
        else:
            return []

    def display_all_books(self):
        if not self.books_by_title:
            print("No books in the library.")
        else:
            for book in self.books_by_title.values():
                print(f"Title: {book['title']}, Authors: {', '.join(book['authors'])}, "
                      f"Genre: {book['genre']}, Year: {book['publication_year']}, Copies: {book['copies']}")



library = LibraryHashTable()

library.add_book("To Kill a Mockingbird", ["Harper Lee"], "Fiction", 1960, copies=5)
library.add_book("1984", ["George Orwell"], "Dystopian", 1949, copies=3)
library.add_book("Animal Farm", ["George Orwell"], "Satire", 1945, copies=4)

print("\nSearch by Title:")
print(library.search_by_title("1984"))

print("\nSearch by Author:")
print(library.search_by_author("George Orwell"))

print("\nAll Books:")
library.display_all_books()
