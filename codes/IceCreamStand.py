class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{self.first_name} {self.last_name}"
        self.login_attempt = 0

    def describe_user(self):
        print(f"The user's name is {self.full_name}")
    
    def greet_user(self):
        print(f"Hello {self.full_name}")

    def reset_login_attempts(self):
        self.login_attempt = 0

    def increment_login_attempts(self):
        self.login_attempt += 1

class Priviledges:
    def __init__(self, priviledges):
        self.priviledges = priviledges

    def show_priviledge(self):
        print("As the admin, you can operate the following content:")
        for priviledge in self.priviledges:
            print(f"-{priviledge}")


class Admin(User):
    def __init__(self, first_name, last_name, priviledges):
        super().__init__(first_name, last_name)
        self.priviledge = Priviledges(priviledges)

priviledges = ['can add post', 'can delete post', 'can ban user']
user_0 = Admin('Shi', 'Quan', priviledges)
user_0.describe_user()
user_0.greet_user()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.reset_login_attempts()
user_0.priviledge.show_priviledge()
print(f"{user_0.full_name} have tried to login in for {user_0.login_attempt} times.")