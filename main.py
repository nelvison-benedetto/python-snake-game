import turtle, random, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import Gameover

screen = turtle.Screen()
#screen.screensize(50,50)
screen.setup(width=600,height=600)
screen.bgcolor("dark blue")
screen.title("The Snake Game!")
screen.tracer(0)
score = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()
gameover = Gameover()

isRunning = True
while isRunning:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
        #print(f"your score is {scoreboard.score}")

    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        #gameover.gameover()
        #isRunning = False
        scoreboard.clear()
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            #gameover.gameover()
            #isRunning = False
            scoreboard.clear()
            scoreboard.reset()
            snake.reset()

    screen.listen()
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="d", fun=snake.right)

screen.exitonclick()


