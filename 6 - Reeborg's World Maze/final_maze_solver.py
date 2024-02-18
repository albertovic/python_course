def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while wall_in_front() == False:
        move()
    turn_left()
    
flag = 0

while at_goal() == False:
    if flag > 4:
        if front_is_clear():
            move()
            while front_is_clear() == False:
                turn_left()
            move()
       
    if right_is_clear() == True:
        turn_right()
        move()
        flag += 1
    elif front_is_clear() == True:
        move()
        flag = 0
    else:
        turn_left()
        