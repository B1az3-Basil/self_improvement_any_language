import random

history = []
join_path = []

the_path = []
obstacles = []


def the_path_list():
    """
    -> This function creates a list of coordinates which ehn they
        are joined together they form a path.
    """
    global the_path
    the_path = [(x, y) for y in range(-190, 191, 20)
                for x in range(-90, 91, 20)]
    return the_path


def back_trace(back_index, the_path):
    """
    -> This function backtraces when there is no where to go
    -> it does this by using a list of coordinates in history
        where is visired then it goes back recursively and tries to
        find another point to go.
    """
    global history
    current_position = history[back_index]
    history.pop()
    four_ways = [(current_position[0] + 20, current_position[1]),
                 (current_position[0] - 20, current_position[1]),
                 (current_position[0], current_position[1] + 20),
                 (current_position[0], current_position[1] - 20)]
    the_ways = [each_way for each_way in four_ways if each_way in the_path]

    if len(the_ways) != 0:
        return the_ways, current_position
    return back_trace(back_index - 1, the_path)


def make_the_path():
    """
    -> this function creates the path by joining the point that is 
        goes to and stores the joined points in a list and a point
        in the history list
    """
    global history, join_path
    history = []
    join_path = []
    the_path = the_path_list()
    current_position = (-90, 190)
    history.append(current_position)
    the_path.remove(current_position)
    while len(the_path) != 0:
        four_ways = [(current_position[0] + 20, current_position[1]),
                     (current_position[0] - 20, current_position[1]),
                     (current_position[0], current_position[1] + 20),
                     (current_position[0], current_position[1] - 20)]
        the_ways = [
            each_way for each_way in four_ways if each_way in the_path and not each_way in history]
        back_index = len(history) - 2
        if len(the_ways) == 0:
            the_ways, current_position = back_trace(back_index, the_path)
        last = current_position
        current_position = the_ways[random.randint(0, len(the_ways) - 1)]
        history.append(current_position)
        if (last[0] > current_position[0] and last[1] == current_position[1]) or \
                (last[1] < current_position[1] and last[0] == current_position[0]):
            join_path.append([current_position, 'Joined', last])
            the_path.remove(current_position)
            continue
        join_path.append([last, 'Joined', current_position])
        the_path.remove(current_position)


def make_rows_and_columns(reset_num, range_first, range_second, decrease):
    """
    -> This function makes the path but this time in rows and colunms 
    -> It stores the each row of coordinats inside a list and 
        stores that list in another list.
        e.g [[(0, 1), (0, 2)]]
    -> It returns them
    """
    x, y = -90, 190
    the_path = []
    if decrease == 1:
        while y > range_first:
            xy = [(x, y) for x in range(x, range_second + 1, 20)]
            the_path.append(xy)
            y -= 20
        return the_path

    while x <= range_first:  # 190, 110 ,-210, 0
        xy = []
        y = reset_num
        xy = [(x, y) for y in range(y, range_second - 1, -20)]
        the_path.append(xy)
        x += 20
    return the_path


def get_row(i, the_path):
    """
    -> This functions takes the points and joins them 
    """
    check_two = 1
    two_coor = []
    index = 0
    while len(the_path[i]) > index:
        if check_two == 1:
            la = the_path[i][index]
            check_two = 2
            index += 1
            continue
        two_coor.append((la, the_path[i][index]))
        check_two = 1
    return get_pos(two_coor)


def get_pos(two_coor):
    """
    -> This function then compares them by using those jointed coordinates
    -> it checks if the joinded coordinats are equal 
    """
    global join_path
    join_ = []
    for i in two_coor:
        for z in join_path:
            if z[0] == i[0] and z[2] == i[1]:
                join_.append(z)
    return join_


def check_between(row, x, y):
    """
    -> This function returns boolean if x, y is in betweeen the row list of coordinates for x-axis
    """
    return len([i for i in row if i[0][0] < x and i[2][0] > x]) == 0


def check_between_y(row, x, y):
    """
    -> This function returns boolean if x, y is in betweeen the row list of coordinates for y-axis
    """
    return len([i for i in row if i[0][1] > y and i[2][1] < y]) == 0


history = []
join_path = []

the_path = []
obstacles = []


def the_path_list():
    """
    -> This function creates a list of coordinates which ehn they
        are joined together they form a path.
    """
    global the_path
    the_path = [(x, y) for y in range(-190, 191, 20)
                for x in range(-90, 91, 20)]
    return the_path


def back_trace(back_index, the_path):
    """
    -> This function backtraces when there is no where to go
    -> it does this by using a list of coordinates in history
        where is visired then it goes back recursively and tries to
        find another point to go.
    """
    global history
    current_position = history[back_index]
    history.pop()
    four_ways = [(current_position[0] + 20, current_position[1]),
                 (current_position[0] - 20, current_position[1]),
                 (current_position[0], current_position[1] + 20),
                 (current_position[0], current_position[1] - 20)]
    the_ways = [each_way for each_way in four_ways if each_way in the_path]

    if len(the_ways) != 0:
        return the_ways, current_position
    return back_trace(back_index - 1, the_path)


def make_the_path():
    """
    -> this function creates the path by joining the point that is 
        goes to and stores the joined points in a list and a point
        in the history list
    """
    global history, join_path
    history = []
    join_path = []
    the_path = the_path_list()
    current_position = (-90, 190)
    history.append(current_position)
    the_path.remove(current_position)
    while len(the_path) != 0:
        four_ways = [(current_position[0] + 20, current_position[1]),
                     (current_position[0] - 20, current_position[1]),
                     (current_position[0], current_position[1] + 20),
                     (current_position[0], current_position[1] - 20)]
        the_ways = [
            each_way for each_way in four_ways if each_way in the_path and not each_way in history]
        back_index = len(history) - 2
        if len(the_ways) == 0:
            the_ways, current_position = back_trace(back_index, the_path)
        last = current_position
        current_position = the_ways[random.randint(0, len(the_ways) - 1)]
        history.append(current_position)
        if (last[0] > current_position[0] and last[1] == current_position[1]) or \
                (last[1] < current_position[1] and last[0] == current_position[0]):
            join_path.append([current_position, 'Joined', last])
            the_path.remove(current_position)
            continue
        join_path.append([last, 'Joined', current_position])
        the_path.remove(current_position)


def make_rows_and_columns(reset_num, range_first, range_second, decrease):
    """
    -> This function makes the path but this time in rows and colunms 
    -> It stores the each row of coordinats inside a list and 
        stores that list in another list.
        e.g [[(0, 1), (0, 2)]]
    -> It returns them
    """
    x, y = -90, 190
    the_path = []
    if decrease == 1:
        while y > range_first:
            xy = [(x, y) for x in range(x, range_second + 1, 20)]
            the_path.append(xy)
            y -= 20
        return the_path

    while x <= range_first:  # 190, 110 ,-210, 0
        xy = []
        y = reset_num
        xy = [(x, y) for y in range(y, range_second - 1, -20)]
        the_path.append(xy)
        x += 20
    return the_path


def get_row(i, the_path):
    """
    -> This functions takes the points and joins them 
    """
    check_two = 1
    two_coor = []
    index = 0
    while len(the_path[i]) > index:
        if check_two == 1:
            la = the_path[i][index]
            check_two = 2
            index += 1
            continue
        two_coor.append((la, the_path[i][index]))
        check_two = 1
    return get_pos(two_coor)


def get_pos(two_coor):
    """
    -> This function then compares them by using those jointed coordinates
    -> it checks if the joinded coordinats are equal 
    """
    global join_path
    join_ = []
    for i in two_coor:
        for z in join_path:
            if z[0] == i[0] and z[2] == i[1]:
                join_.append(z)
    return join_


def check_between(row, x, y):
    """
    -> This function returns boolean if x, y is in betweeen the row list of coordinates for x-axis
    """
    return len([i for i in row if i[0][0] < x and i[2][0] > x]) == 0


def check_between_y(row, x, y):
    """
    -> This function returns boolean if x, y is in betweeen the row list of coordinates for y-axis
    """
    return len([i for i in row if i[0][1] > y and i[2][1] < y]) == 0


def get_obstacles():
    """
    -> This function creates the obstacle list if coordinates
    """
    global obstacles
    obstacles = []
    make_the_path()
    x, y = -80, 200
    i = 0
    while y > -200:
        x = -80
        if y % 20 == 0:
            row = get_row(i, make_rows_and_columns(-90, -210, 110, 1))
            i += 1
        while x <= 100:
            if check_between(row, x, y):
                obstacles.append((x, y - 4))
            x += 20
        y -= 4
    i = 0
    x, y = -100, 200
    while x < 100:
        y = 200

        if x % 20 == 0:
            row = get_row(i, make_rows_and_columns(190, 110, -210, 0))
            i += 1

        while y > -190:
            if check_between_y(row, x, y):
                obstacles.append((x, y))
            y -= 20
        x += 4
    obstacles = [obs for obs in obstacles if obs[1] != 200 and obs[0]
                 != 100 and obs != (0, 0) and obs != (0, -4) and obs != (-4, 0)]
    points = [(obs[0] + 4, obs[1])for obs in obstacles if (obs[0] + 4,
                                                           obs[1] - 4) in obstacles
              and not (obs[0], obs[1] + 4) in obstacles]
    obstacles = obstacles + points
    return obstacles


def is_path_blocked(x1, y1, x2, y2):
    '''
    -> This function gets the current position and the future position
    -> Then it uses the positins to determine if there is a obstacle in front and back of the robot
    -> It returns True if its not there and returns False if its there 
    '''

    for each_obstacle in obstacles:
        x, y = each_obstacle
        if x1 == x2:
            if x <= x1 <= x + 4 and y <= y2 and y1 <= y + 4:
                return True

            elif x <= x1 <= x + 4 and y + 4 >= y2 and y1 >= y and y1 > y2:
                return True

        elif y1 == y2:

            if y <= y1 <= y + 4 and x <= x2 and x1 <= x + 4:
                return True

            elif y <= y1 <= y + 4 and x + 4 >= x2 and x1 >= x:
                return True

    return False


def is_path_blocked(x1, y1, x2, y2):
    '''
    -> This function gets the current position and the future position
    -> Then it uses the positins to determine if there is a obstacle in front and back of the robot
    -> It returns True if its not there and returns False if its there 
    '''

    for each_obstacle in obstacles:
        x, y = each_obstacle
        if x1 == x2:
            if x <= x1 <= x + 4 and y <= y2 and y1 <= y + 4:
                return True

            elif x <= x1 <= x + 4 and y + 4 >= y2 and y1 >= y and y1 > y2:
                return True

        elif y1 == y2:

            if y <= y1 <= y + 4 and x <= x2 and x1 <= x + 4:
                return True

            elif y <= y1 <= y + 4 and x + 4 >= x2 and x1 >= x:
                return True

    return False


def is_position_blocked(x, y):
    '''
    -> This function checks if the position of the obstacle is already taken 
    '''
    return True in [1 == 1 for each_obstacle in obstacles if 
            (each_obstacle[0] <= x <= each_obstacle[0] + 4
            and each_obstacle[1] <= y <= each_obstacle[1] + 4)]
