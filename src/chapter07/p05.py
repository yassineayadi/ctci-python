"""
**Online Book Reader**:

Design the datastructure for an online book reader.
"""

# Questions:
# * do we care about a payment system?
# * can it support multiple stores? (does it have a browser?)
# * do we focus only on the core functionalities?

# Objects:
# * Reader
# * Book (Progression) Readidng/Read
# * Page
# * lines/words
# * Sources (Stores/Email/Local Storage)

# * Actions:
# * Download Book
# * Highlight
# * Turn page (left and right)
# * bookmark/notes

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Line:
    words: List[str]


@dataclass
class Page:
    lines: List[Line]
    number: int


@dataclass
class Book:
    title: str
    pages: List[Page]

    @property
    def length(self):
        return len(self.pages)


@dataclass
class ReaderBook(Book):

    current_page: Page = field(default=None)
    read_pages: List[Page] = field(default_factory=lambda: list)

    @property
    def progression(self) -> float:
        """Returns the % of number of pages read."""
        return len(self.read_pages) / len(self.pages)

    @classmethod
    def from_book(cls, book: Book) -> "ReaderBook":
        attrs = vars(book)
        return cls(**attrs)

    def start_from_the_beginning(self):
        self.current_page = self.pages[0]

    @property
    def current_page_number(self):
        return self.current_page.number

    def next_page(self):
        if self.current_page.number < self.length:
            self.current_page = self.pages[self.current_page_number + 1]

    def previous_page(self):
        if self.current_page.number > 0:
            self.current_page = self.pages[self.current_page_number - 1]


class BookNotFound(Exception):
    """Raised by a store if the book is not found in the store's catalog."""


class Store:
    available_books: Dict[str, Book]

    def search_book(self, book_title):
        if book_title in self.available_books:
            return self.available_books[book_title]
        else:
            raise BookNotFound(f"Book '{book_title}' cannot be found our catalog.")


@dataclass
class Reader:
    available_books: Dict[str, ReaderBook]
    current_book: ReaderBook

    def read_book(self, book_title):
        self.current_book = self.available_books[book_title]

    def download_book(self, store: Store, book_title: str):
        book = store.search_book(book_title)
        if book:
            reader_book = ReaderBook.from_book(book)
            self.available_books[book_title] = reader_book

    def start_book(self, book_tile: str):
        self.current_book = self.available_books[book_tile]

    def next_page(self):
        if self.current_book:
            self.current_book.next_page()

    def previous_page(self):
        if self.current_book:
            self.current_book.previous_page()
