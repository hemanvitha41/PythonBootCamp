import random
import	time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)
player = Player()
game_is_on = True
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:
	time.sleep(0.1)
	screen.update()

	car_manager.create_car()
	car_manager.move_cars()

	# Detect collision with car
	for car in car_manager.cars:
		if car.distance(player) < 20:
			scoreboard.game_over()
			screen.update()  # Update the screen to display "GAME OVER"
			time.sleep(2)  # Pause for 2 seconds to let the user see the message
			game_is_on = False

	# Detect crossing
	if player.is_at_finish_line():
		player.go_to_start()
		car_manager.increase_speed()
		scoreboard.increase_level()
