from .models import Author, Book, Library, Librarian

# Retrieving all books by a particular author
author_name = "danamaz knows"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# Listing all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# librarian of a library
library = Library.objects.get(name=library_name)
librarian_of_libary = library.liberian

# librarian_of_libary = Librarian.objects.get(library_id=1)
