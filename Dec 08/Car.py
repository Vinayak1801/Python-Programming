class Car:
    def __init__(self,color,price,kilometer):
        self.color = color
        self.price = price
        self.kilometer = kilometer

    def compare_price(self, other_car):
        if self.price > other_car.price:
            return f"{self.color} car is expensive than {other_car.color} car."
        elif self.price < other_car.price:
            return f"{other_car.color} car is expensive than {self.color} car."
        else:
            return "Both cars have same price."

    def add_kilometers(self, other_car):
        total_kilometers = self.kilometer + other_car.kilometer
        return f"The total kilometers of the two cars is {total_kilometers} km."


car1 = Car("Red", 500000, 21000)
car2 = Car("Blue", 700000, 29000)

print(car1.compare_price(car2))
print(car1.add_kilometers(car2))


