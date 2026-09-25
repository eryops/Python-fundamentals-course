class User:
    pass

class AdminUser(User):
    pass

admin = AdminUser()

print(isinstance(admin, AdminUser))   # True
print(isinstance(admin, User))        # True
print(isinstance(admin, str))         # False
