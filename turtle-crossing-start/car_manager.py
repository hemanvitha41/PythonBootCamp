from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """Manage multiple car objects."""
        self.cars = []  # List to store car objects
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a new car with random properties."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)  # Start off-screen on the right
            self.cars.append(new_car)

    def move_cars(self):
        """Move all cars left by the current move distance."""
        for car in self.cars:
            car.backward(self.move_distance)

    def increase_speed(self):
        """Increase the speed of the cars."""
        self.move_distance += MOVE_INCREMENT
