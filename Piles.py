from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.

#to make karel pick up beepers
def pickup_all_beepers():
    for i in range(10):
        pick_beeper()

#to make karel move two times
def move_more():
    for i in range(2):
        move()

def main():
    move()
    pickup_all_beepers()
    move_more()
    pickup_all_beepers()
    move_more()
    pickup_all_beepers()
    move()
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
