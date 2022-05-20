# Reeborg'sWorld_allHurdles_cheatcode
# Created by Cephas Cardozo
# Developed using Python

# functions
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
  
# loop
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
# loop  
    while front_is_clear():
        move()
    turn_left()

# loop
while not at_goal():
  
# conditionals
    if wall_in_front():
        hurdle()
    else:
        move()