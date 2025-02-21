from abc import ABC, abstractmethod
import logging
from typing import List

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("book_log.log"), logging.StreamHandler()],
)


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self) -> None:
        for book in self.books:
            logging.info(book)


class LibraryManager:
    def __init__(self, library: Library) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        self.library.add_book(title, author, year)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.error("Invalid command")


if __name__ == "__main__":
    main()
