class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def update_email(self, email):
        self.email = email

    def __repr__(self):
        return f'Username: {self.username}, User email: {self.email}'

class AdminUser(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level or 0

    def update_admin_level(self, level):
        self.admin_level = level

    def __repr__(self):
            return f'Username: {self.username}, User email: {self.email}, Admin Level: {self.admin_level}'

class PremiumUser(User):
    def __init__(self, username, email, premium_points):
        super().__init__(username, email)
        self.premium_points = premium_points or 0

    def update_premium_points(self, points):
        if (points + self.premium_points) < 0:
            self.premium_points = 0
        else: 
            self.premium_points += points

    def __repr__(self):
        return f'Username: {self.username}, User email: {self.email}, Premium points: {self.premium_points}'
       

        
