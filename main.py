from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#TODO 1:Create a snake
snake_game = Snake()
#TODO 2:Create Food for snake
snake_food = Food()
#TODO 3:Create Scoreboard to keep track of score
snake_score = Scoreboard()

screen.listen()
screen.onkey(snake_game.up, "Up")
screen.onkey(snake_game.down, "Down")
screen.onkey(snake_game.left, "Left")
screen.onkey(snake_game.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_game.move()

#check food collision
    if snake_game.head.distance(snake_food) < 15:
        snake_food.refresh()
        snake_score.increase_score()
        snake_game.extend()

#Detect collision with wall
    if snake_game.head.xcor() > 285 or snake_game.head.xcor() < -285 or snake_game.head.ycor() > 285 or snake_game.head.ycor() < -285:
        game_is_on = False
        snake_score.game_over()
#Detect collision with tail
    for segment in snake_game.snake[1:]:
        if snake_game.head.distance(segment) < 10:
            game_is_on = False
            snake_score.game_over()


screen.exitonclick()