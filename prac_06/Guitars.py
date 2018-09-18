class Guitars:
    def __init__(self, name, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def str(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2018 - self.year
        return "The {} is 2018 - {} = {}".format(self.name, self.year, age)

    def is_vintage(self):
        if (2018 - self.year) >= 50:
            return "{} is vintage.format(self.name)"

