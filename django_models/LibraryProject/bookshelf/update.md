```python
from bookshelf.models import Book

# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)

# Expected Output:
# Nineteen Eighty-Four
# The book title has been successfully updated.
```
