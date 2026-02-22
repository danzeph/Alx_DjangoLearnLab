import requests

# CONFIGURATION

BASE_URL = "http://127.0.0.1:8000/api/"
BOOK_LIST_URL = BASE_URL + "books/"
BOOK_CRUD_URL = BASE_URL + "book_all/"


# TOKEN = "My_token_can't be viewed here so i will rather paste in the terminal"
TOKEN = input("Enter your token: ")

headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}


# GET BOOKS (All Authenticated Users)
def get_books():
    response = requests.get(BOOK_LIST_URL, headers=headers)

    print("GET BOOKS RESPONSE:")
    print("Status:", response.status_code)
    data = response.json()
    if response.status_code == 200:
        for book in data["results"]:
            print(book)
    else:
        print(data)

# CREATE BOOK (Admin Only)
def create_book():
    data = {
        "title": "New API Book",
        "author": "System Script",
        "published_date":"2010-01-13",
    }

    response = requests.post(
        BOOK_CRUD_URL,
        headers=headers,
        json=data
    )

    print("\n CREATE BOOK RESPONSE:")
    print("Status:", response.status_code)
    print(response.json())


# UPDATE BOOK (Admin Only)
def update_book(book_id):
    url = f"{BOOK_CRUD_URL}{book_id}/"

    data = {
        "title": "Updated Book Title"
    }

    response = requests.patch(
        url,
        headers=headers,
        json=data
    )

    print("\n UPDATE BOOK RESPONSE:")
    print("Status:", response.status_code)
    print(response.json())


# DELETE BOOK (Admin Only)
def delete_book(book_id):
    url = f"{BOOK_CRUD_URL}{book_id}/"

    response = requests.delete(url, headers=headers)

    print("\n DELETE BOOK RESPONSE:")
    print("Status:", response.status_code)


# TEST WITHOUT TOKEN
def test_without_token():
    response = requests.get(BOOK_LIST_URL)

    print("\n WITHOUT TOKEN RESPONSE:")
    print("Status:", response.status_code)
    print(response.text)


# MAIN TEST RUN
if __name__ == "__main__":
    print("Testing API Authentication & Permissions...\n")

    test_without_token()   # Should return 401

    get_books()            # Should work if token valid

    create_book()          # Works ONLY if admin token

    update_book(8)         # Change ID if needed and works only for admin/superuser

    delete_book(13)         # Change ID if needed and only works for admin/superuser


# Check Results with different tokens (admin/superuser and other user) in the auth_script.md
