from karel.stanfordkarel import 

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""
def mov():
    move()
    move()

def turn_right():
    turn_left()
    turn_left()

def main():
   mov()
   pick_beeper()
   move()
   turn_left()
   mov()
   put_beeper()
   turn_right()
   mov()
   turn_right()
   turn_left()
   mov()
   move()
   turn_right()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
