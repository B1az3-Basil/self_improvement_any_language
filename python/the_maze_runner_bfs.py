import time
import battle_maze
import turtle 

obstacles = battle_maze.get_obstacles()
# obstacles = []

def draw_turtle():
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

def area51(x, y):
    return -100 <= x <= 100 and -200 <= y <= 200

step = 5
    
def bfs_solve():

    space = [(x,y) for x in range(-100, 101, step) for y in range(-200, 201, step) if not battle_maze.is_position_blocked(x,y)]
    # print(space)
    x, y = -100, 200
    
    # print((0, 7) in space)
    draw_turtle()
    position = [{1:(0,0)}]
    star_coor = [(0,0)]
    x, y = 0, 0
    to_get = (0, 0)
    turtle.delay(1)
    turtle.penup()
    check = True
    index = 2
    for x in position:
        # print(x)
        index = list(x.keys())[0] + 1
        x = list(x.values())[0]
        # star_coor.append(x)
        # print(star_coor)
        if (x[0] + step, x[1]) in space and not (x[0] + step, x[1]) in star_coor:
            turtle.goto(x[0] + step, x[1])
            star_coor.append((x[0] + step, x[1]))
            position.append({index:(x[0] + step, x[1])})
            turtle.stamp()
            print("right", (x[0] + step, x[1]))

        if (x[0] - step, x[1]) in space and not (x[0] - step, x[1]) in star_coor:
            turtle.goto(x[0] - step, x[1])
            star_coor.append((x[0] - step, x[1]))
            position.append({index: (x[0] - step, x[1])})
            turtle.stamp()
            print('left', (x[0] - step, x[1]))

        if (x[0], x[1] + step) in space and not (x[0], x[1] + step) in star_coor:
            turtle.goto(x[0], x[1] + step)
            star_coor.append((x[0], x[1] + step))
            position.append({index: (x[0], x[1] + step)})
            turtle.stamp()
            print("up", (x[0], x[1] + step))
        
        if (x[0], x[1] - step) in space and not (x[0], x[1] - step) in star_coor:
            turtle.goto(x[0], x[1] - step)
            star_coor.append((x[0], x[1] - step))
            position.append({index : (x[0], x[1] - step)})
            turtle.stamp()
            print("down", (x[0], x[1] + step))
        
        if x[1] + step == 200:
            to_get = (x[0], 200)
            break

        # if index == 2:
        #     break
    
    the_path = []   
    print("found")
    turtle.pendown()
    index -= 1
    turtle.pencolor("green")
    while index != 0:
        if {index: (to_get[0], to_get[1] - step)} in position:
            to_get = (to_get[0], to_get[1] - step)
            turtle.goto(to_get)
            the_path.append(to_get)
            index -= 1

        elif {index: (to_get[0], to_get[1] + step)} in position:
            to_get = (to_get[0], to_get[1] + step)
            turtle.goto(to_get)
            the_path.append(to_get)
            index -= 1

        elif {index: (to_get[0] - step, to_get[1])} in position:
            to_get = (to_get[0] - step, to_get[1])
            turtle.goto(to_get)
            the_path.append(to_get)
            index -= 1

        elif {index: (to_get[0] + step, to_get[1])} in position:
            to_get = (to_get[0] + step, to_get[1])
            turtle.goto(to_get)
            the_path.append(to_get)
            index -= 1


    input()

bfs_solve()

