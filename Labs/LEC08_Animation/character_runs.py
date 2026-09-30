from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
frame = 0
action = 0

while(1):
    
    if action % 2 == 0:
        r = range(800, 0, -15)
    else:
        r = range(0, 800, 15)
 
    for x in r:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(
            frame * FRAME_WIDTH, action * FRAME_HEIGHT,
            FRAME_WIDTH, FRAME_HEIGHT,
            x, 110,
            200, 200
        )
        update_canvas()

        frame = (frame + 1) % 8
        delay(0.07)
    action = (action + 1) % 4

close_canvas()

