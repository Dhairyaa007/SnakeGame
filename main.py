from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

X_POS_COR = 750
X_NEG_COR = -750
Y_POS_COR = 390
Y_NEG_COR = -390

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("SNAKE GAME")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.replay, "w")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > X_POS_COR or snake.head.xcor() < X_NEG_COR or \
            snake.head.ycor() > Y_POS_COR or snake.head.ycor() < Y_NEG_COR:
        game_is_on = False
        score.game_over()
        snake.replay()

    for seg in snake.segments_list[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()
            snake.replay()

s.exitonclick()
