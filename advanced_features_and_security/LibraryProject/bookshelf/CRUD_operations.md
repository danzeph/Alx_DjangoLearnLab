# CRUD Operations in Django Shell

---

## Create

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```

Output:
```
<Book: Book object (1)>
```

---

## Retrieve

```python
book = Book.objects.get(title="1984")

print(book.title)
print(book.author)
print(book.publication_year)
```

Output:
```
1984
George Orwell
1949
```

---

## Update

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)
```

Output:
```
Nineteen Eighty-Four
```

---

## Delete

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
```

Output:
```
<QuerySet []>
```

---
