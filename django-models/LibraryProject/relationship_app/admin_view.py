def is_admin(user):
    if not user.is_authenticated:
        return False
    return user.userprofile.role == "admin"
