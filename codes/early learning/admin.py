from user import User

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