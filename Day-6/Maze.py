def turn():
    turn_left()
    turn_left()
    turn_left()
while not is_facing_north():
    turn_left()
while front_is_clear():
    move()
while not at_goal():   
    if right_is_clear():
        turn()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
