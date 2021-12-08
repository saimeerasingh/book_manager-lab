from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("J.K","Rowling")
author_repository.save(author1)
author2 = Author("Adam","Kay")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Harry Potter","Fiction",10,author1)
book_repository.save(book1)

book2 = Book("This is going to hurt","Biography",12,author2)
book_repository.save(book2)

