import battle_maze
import turtle

obstacles = battle_maze.get_obstacles()
# obstacles = []
space = []
step = 5
def draw_turtle():
    global space
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(100, 200)
    turtle.pendown()
    turtle.goto(-100, 200)
    turtle.goto(-100, -200)
    turtle.goto(100, -200)
    turtle.goto(100, 200)
    turtle.pencolor("black")
    turtle.fillcolor("red")
    turtle.tracer(0)
    for obs in obstacles:
        turtle.penup()
        turtle.goto(obs)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.fd(4)
            turtle.lt(90)
        turtle.end_fill()
    turtle.tracer(1)
    turtle.penup()
    turtle.goto(0,0)
    turtle.left(90)
    turtle.turtlesize(0.1, 0.1)
    turtle.shape("square")
    space = [(x,y) for x in range(-100, 101, step) for y in range(-200, 201, step) if not battle_maze.is_position_blocked(x,y)]