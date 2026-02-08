```python
from bookshelf.models import Book

# Retrieve the book and display all its attributes
book = Book.objects.get(title="1984")

print(book.title)
print(book.author)
print(book.publication_year)

# Expected Output:
# 1984
# George Orwell
# 1949
```
