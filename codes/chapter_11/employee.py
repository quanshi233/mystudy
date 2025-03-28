class Employee:
    def __init__(self, first_name, last_name, salary, middle_name=''):
        if middle_name:
            self.full_name = f"{first_name} {middle_name} {last_name}"
        else:
            self.full_name = f"{first_name} {last_name}"
        self.salary = int(salary)
    
    def give_raise(self, increment='5000'):
        increment = int(increment)
        self.salary += increment