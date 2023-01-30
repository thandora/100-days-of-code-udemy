#
# Only works at reeborg:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


redundancy_counter = 0
while not at_goal():
    # Edge case
    # If robot turns right 4 times in a row with no walls on its right, force to turn left to break cycle.
    if redundancy_counter == 4:
        turn_left()
        redundancy_counter = 0
    if right_is_clear():
        turn_right()
        move()
        redundancy_counter += 1
    elif front_is_clear():
        move()
        redundancy_counter = 0
    else:
        turn_left()
        redundancy_counter = 0


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
