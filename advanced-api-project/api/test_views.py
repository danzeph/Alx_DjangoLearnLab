from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITest(APITestCase):

    def setUp(self):
        """
        Create test user, author, and book.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

        self.author = Author.objects.create(name="George Orwell")

        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])


    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')

        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2020,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_book(self):
        self.client.login(username='testuser', password='password123')

        data = {
            "title": "Updated Title",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_book(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_filter_books(self):
        response = self.client.get(self.list_url + '?publication_year=1949')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=1984')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_order_books(self):
        response = self.client.get(self.list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)