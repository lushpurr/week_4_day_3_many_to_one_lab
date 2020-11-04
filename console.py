import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()
# title, genre, publisher, author,  id = None


author_1 = Author("JK", "Rowling")
author_repository.save(author_1)
author_2 = Author("Jesus", "Christ")
author_repository.save(author_2)

book1 = Book("Harry Potter", "Fiction", "Penguin", author_1)
book_repository.save(book1)
book2 = Book("Matilda", "Fiction", "Roald Dahl", author_2)
book_repository.save(book2)

book_repository.select_all()


pdb.set_trace()