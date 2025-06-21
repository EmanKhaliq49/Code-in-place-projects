from graphics import Canvas
import random, time, os, math, sys

# ───── constants ─────
W, H          = 400, 400
BALL_SIZE     = 25
R2            = (BALL_SIZE/2)**2            # radius²
HOOP_X1, HOOP_Y1 = 190, 20
HOOP_X2, HOOP_Y2 = 240, 70
BASELINE_Y    = H - 30
GOAL_DISPLAY_SEC = 0.5                      # “GOALLLLL” kitni der dikhayen?

# ───── helpers ─────
def add_bg(cv):
    if os.path.exists("basketball_court.jpg"):
        cv.create_image_with_size(0, 0, W, H, "basketball_court.jpg")

def add_title(cv):
    cv.create_text(W/2, H/4,
                   text="BASKETBALL GAME",
                   font="Monospace", font_size=40,
                   color="grey", anchor="center")

def add_hoop(cv):
    for i in range(5):
        line = cv.create_line(180, 20, 250, 20, 'orange')
    
    x1 = 190
    while(x1<=240):
        line = cv.create_line(x1, 20, 220, 70, 'black')
        x1 += 10
    
    line = cv.create_line(195, 30, 235, 30, 'black')
    line = cv.create_line(200, 40, 233, 40, 'black')
    line = cv.create_line(206, 50, 229, 50, 'black')
    
    return cv.create_rectangle(HOOP_X1, HOOP_Y1, HOOP_X2, HOOP_Y2,
                               "transparent")

def random_baseline_x():
    return random.randint(10, W-BALL_SIZE-10)

def click_xy(c):
    if c is None: return None, None
    if isinstance(c, dict): return c.get('x'), c.get('y')
    if isinstance(c, (list, tuple)): return c[0], c[1]
    if hasattr(c, 'x') and hasattr(c, 'y'): return c.x, c.y
    return None, None

def click_hits(cx, cy, left, top):
    return (cx-left-BALL_SIZE/2)**2 + (cy-top-BALL_SIZE/2)**2 <= R2

# ───── main loop ─────
def main():
    cv = Canvas(W, H)
    add_bg(cv)
    title_id = add_title(cv)
    hoop_id  = add_hoop(cv)

    ball_id = cv.create_oval(10, BASELINE_Y,
                             10+BALL_SIZE, BASELINE_Y+BALL_SIZE,
                             "orange", "black")

    following = True
    goal_time = None       # None means goal banner not showing
    banner_id = None

    while True:
        # --- quit check ---
        for key in cv.get_new_key_presses():
            if key == '1' or key:     # koi bhi key chalegi, '1' khas
                sys.exit()

        # --- goal banner active? ---
        if goal_time is not None:
            if time.time() - goal_time >= GOAL_DISPLAY_SEC:
                cv.delete(banner_id)
                banner_id = None
                goal_time = None
                following = True      # reset to mouse control
            time.sleep(0.01)
            continue                  # skip rest until banner done

        if following:
            # move with mouse
            mx, my = cv.get_mouse_x(), cv.get_mouse_y()
            if mx is not None and my is not None:
                cv.moveto(ball_id, mx-BALL_SIZE/2, my-BALL_SIZE/2)

            # goal check
            left, top = cv.coords(ball_id)
            if hoop_id in cv.find_overlapping(left, top,
                                              left+BALL_SIZE, top+BALL_SIZE):
                # score!
                cv.moveto(ball_id, random_baseline_x(), BASELINE_Y)
                banner_id = cv.create_text(W/2, H/2,
                                           text="GOALLLLL",
                                           font="Impact", font_size=60,
                                           color="red", anchor="center")
                goal_time = time.time()
                following = False     # freeze until reset

        else:
            # waiting for click on ball
            for click in cv.get_new_mouse_clicks():
                cx, cy = click_xy(click)
                left, top = cv.coords(ball_id)
                if click_hits(cx, cy, left, top):
                    following = True
                    break

        time.sleep(0.01)

if __name__ == "__main__":
    main()