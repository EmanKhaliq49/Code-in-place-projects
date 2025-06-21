from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)        
    top_y_start = CANVAS_HEIGHT - BOX_SIZE 
    total_boxes_width = N_BOXES * BOX_SIZE

    # Calculate the starting x-coordinate to center the line of boxes
    # This ensures the entire line of boxes is centered horizontally
    start_x_offset = (CANVAS_WIDTH - total_boxes_width) / 2

    # Loop to create each box
    # The 'i' variable represents the current box's index (0 to N_BOXES-1)
    for i in range(N_BOXES):
        # Calculate the left_x coordinate for the current box
        # This is the starting offset plus the horizontal position based on 'i'
        left_x = start_x_offset + (i * BOX_SIZE)

        # Calculate the other coordinates for the rectangle
        # The top_y is constant for all boxes in the line
        top_y = top_y_start
        # The right_x is the left_x plus the BOX_SIZE
        right_x = left_x + BOX_SIZE
        # The bottom_y is the top_y plus the BOX_SIZE
        bottom_y = top_y + BOX_SIZE

        # Create Point objects for the top-left and bottom-right corners
        # These points define the bounding box of the rectangle
        rect = canvas.create_rectangle(left_x, top_y,right_x, bottom_y, "white", "black")
        

        

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    
