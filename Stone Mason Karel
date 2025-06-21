from karel.stanfordkarel import *

#to put the beeper till the top
def put_column():
    while(front_is_clear()):
        put_beeper()
        move()
    put_beeper()

#to move the karel to the next arches
def move_to_next_arch():
        for i in range(4):
          move()

#to make karel turn right
def turn_right():
    for x in range(3):
        turn_left()

#to make karel go back to initial position
def move_back():
    while(front_is_clear()):
        move()

#to make karel turn towards down and move
def move_to_initial():
    turn_left()
    turn_left()
    move_back()

#to make karel move and put beepers till the end
def build_columns():
    while(front_is_clear()):
     turn_left()
     put_column()
     move_to_initial()
     turn_left()
     move_to_next_arch()

#main function to execute the program
def main():
   build_columns()
   turn_left()
   put_column()
   move_to_initial()
   turn_left()

if __name__ == '__main__':
    main()
