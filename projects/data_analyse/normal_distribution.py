from random import choice

class N_D:
    def __init__(self, steps=20, samples=1000):
        self.x_value = range(-20,21)
        self.steps = steps
        self.samples = samples
        self.result = []

    def get_rn(self):
        a = 0
        b = 0
        while a < self.steps:
            a_b = choice([-1,1])
            a += 1
            b += a_b
        return b
    
    def fill_walk(self):
        a = 0
        while a < self.samples:
            self.result.append(self.get_rn())
            a += 1