from karel.stanfordkarel import *

#to make karel put beepers and move forward
def fill_beepers():
    while(front_is_clear()):
        put_beeper()
        move()
    put_beeper()

#to make karel turn right
def turn_right():
    for i in range(3):
        turn_left()

#to make karel go back
def move_back():
    while(front_is_clear()):
        move()

#to make karel move on the upper row
def move_up():
    if(right_is_clear()):
        turn_right()
        move()

#to move karel
def move_forward():
    while(front_is_clear()):
        move()

#to make karel fill its world with beepers
def put_beeper_in_world():
    while(front_is_clear()):
        fill_beepers()
        turn_left()
        turn_left()
        move_back()
        move_up()
        turn_right()

#main function
def main():
   put_beeper_in_world()
   move_up()
   move_forward()
  
if __name__ == '__main__':
    main()
