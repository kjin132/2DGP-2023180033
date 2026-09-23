## 여기를 채우시오.


from pico2d import *
open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

xy = [400, 300]
dirx = [8, 0, -8, 0]
diry = [0, -8, 0, 8]
idx = 0
n = 0
running = True
while running:
    clear_canvas()
    if idx == 0 and xy[0] > 750:
        idx = 1
    elif idx == 1 and xy[1] < 50:
        idx = 2
    elif idx == 2 and xy[0] < 50:
        idx = 3
    elif idx == 3 and xy[1] > 550:
        idx = 0

    xy[0] += dirx[idx]
    xy[1] += diry[idx]
    clear_canvas()
    character.draw(xy[0], xy[1])
    update_canvas()
    delay(0.01)

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # X 버튼을 눌렀을 때
            running = False

close_canvas()

# import math

# running = True
# center_x , center_y = 400, 300
# radius = 150
# angle = 0
# speed = 2

# while running:

#     clear_canvas()

#     x = center_x + radius * math.cos(angle)
#     y = center_y + radius * math.sin(angle)

#     character.draw(x, y)

#     update_canvas()
    
#     angle += math.radians(speed)

#     delay(0.01)

#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT: # X 버튼을 눌렀을 때
#             running = False

# close_canvas()