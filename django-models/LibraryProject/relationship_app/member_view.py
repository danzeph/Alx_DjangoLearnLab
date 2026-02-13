def is_member(user):
   if user.userprofile.role != "Member":
       return False
   return True

