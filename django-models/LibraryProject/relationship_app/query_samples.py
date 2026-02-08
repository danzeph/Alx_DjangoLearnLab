from .models import Author, Book, Library, Librarian

# Retrieving all books by a particular author
author = Author.objects.get(name='danamaz')
books_by_author = author.books.all()

# Listing all books in a library
library = Library.objects.get(id=1)
books_in_library = library.books.all()

# librarian of a library
library = Library.objects.get(id=2)
librarian_of_libary = library.liberian

# librarian_of_libary = Librarian.objects.get(library_id=1)


