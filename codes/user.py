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