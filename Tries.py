class TrieNode:
    def __init__(self):
        self.children = {}
        self.books = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, book):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.books.append(book)

    def search(self, key):
        # Traverse to the node matching the key prefix
        node = self.root
        for char in key:
            if char not in node.children:
                return []  # No match
            node = node.children[char]
        return self._collect_books(node)

    def _collect_books(self, node):
        # Recursive function to collect all books in the subtree
        books = list(node.books)
        for child in node.children.values():
            books.extend(self._collect_books(child))
        return books


class LibraryTrie:
    def __init__(self):
        self.trie_by_title = Trie()
        self.trie_by_author = Trie()

    def add_book(self, title, authors, genre, publication_year, isbn=None, copies=1):
        book = {
            "title": title,
            "authors": authors,
            "genre": genre,
            "publication_year": publication_year,
            "isbn": isbn,
            "copies": copies,
        }
        self.trie_by_title.insert(title.lower(), book)
        for author in authors:
            self.trie_by_author.insert(author.lower(), book)

    def search_by_title(self, title):
        return self.trie_by_title.search(title.lower())

    def search_by_author(self, author):
        return self.trie_by_author.search(author.lower())



library = LibraryTrie()

library.add_book("To Kill a Mockingbird", ["Harper Lee"], "Fiction", 1960, copies=5)
library.add_book("1984", ["George Orwell"], "Dystopian", 1949, copies=3)
library.add_book("Animal Farm", ["George Orwell"], "Satire", 1945, copies=4)

print("\nSearch by Title (Partial):")
print(library.search_by_title("198"))

print("\nSearch by Author (Partial):")
print(library.search_by_author("Geo"))
