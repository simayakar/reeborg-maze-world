def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    count = 0
    i = 0
    turn_left()
    while right_is_clear() != True:
        move()
        count = count + 1
    turn_right()
    move()
    turn_right()
    while i != count:
        move()
        i = i + 1
    turn_left()


while at_goal() != True:
    if wall_in_front() != True:
        move()
    elif right_is_clear() == True:
        turn_right()
        move()
    else:
        turn_left()
