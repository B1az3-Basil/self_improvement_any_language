import draw_maze
import turtle
import time

visited = []
choosen = []
space = []
class node():
    def __init__(self, g_cost = 200, h_cost = 1, f_cost = 201, coor = (0, 0)):
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = f_cost
        self.coor = coor


    def create_node(self, y_value, h_cost, coor):
        self.coor = coor
        self.g_cost = 200 - y_value
        self.h_cost = h_cost
        self.f_cost = self.g_cost + h_cost
        

    def __ge__(self, other):
        # print("greater than")
        return self.f_cost >= other.f_cost


    # def __lt__(self, other):
    #     # print("less than")
    #     return self.g_cost < other.g_cost
    
    
    # def __eq__(self, other):
    #     print("equal")
    #     return self.f_cost == other.f_cost


def check_the_lower(position):

    visited_new = [i for i in visited]
    for z in choosen:
        visited_new.remove(z)

    while len(visited_new) != 1:
        if visited_new[0] >= visited_new[-1]:
            visited_new.remove(visited_new[0])
        
        # elif visited_new[0] == visited_new[-1]:
        #     print("True")
        #     if visited_new[-1] < visited_new[0]:
        #         visited_new.remove(visited_new[0])
        #     else:
        #         visited_new.remove(visited_new[-1])
        else:
            visited_new.remove(visited_new[-1])

    return visited_new[0].coor, visited_new[0]


step = 5
def check_if_there(coor, index):
    while index != len(visited):
        if visited[index].coor == coor:
            return True
        index += 1
    return False
    
    
def bfs_solve():
    global visited, choosen, space
    new_node = node()
    visited = [new_node]
    choosen = [new_node]
    h_cost = 2
    total = new_node
    space = draw_maze.space
    position = (0,0)
    four_ways = [(0, -step), (step, 0), (-step, 0), (0, step)]
    turtle.penup()
    space.remove((0,0))
    turtle.delay(1)
    while True:
        h_cost = total.h_cost
        for each_side in four_ways:
            x1, y1 = each_side
            x2, y2 = position
            coor = (x2 + x1, y2 + y1)
            
            if check_if_there(coor, 0) or not coor in space:
                continue
            
            # print(h_cost)
            new_node = node()
            new_node.create_node(coor[1],h_cost + 1, coor)
            turtle.goto(coor)
            turtle.stamp()
            visited.append(new_node)
            # time.sleep(5)
      
        position, total = check_the_lower(position)
        choosen.append(total)
        # print(position)
    

        if position[1] == 200:
            break
      
    
    the_path = []   
    print("found")
    turtle.pendown()
    # index -= 1
    turtle.pencolor("green")
    while h_cost != 1:
        if {index: (to_get[0], to_get[1] - step)} in choosen:
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


    
if __name__ == "__main__":
    draw_maze.draw_turtle()
    bfs_solve()
    input()