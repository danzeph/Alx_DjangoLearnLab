def is_librarian(user):
    if user.userprofile.role != "Librarian":
        return False
    return True

