from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    rect = canvas.create_rectangle(0, CANVAS_HEIGHT/2, CANVAS_WIDTH, 0, "red")

if __name__ == '__main__':
    main()
