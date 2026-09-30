import os

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
SHEET_FILE = 'warrior_sheet.png'
SHEET_W, SHEET_H = 256, 171
CELL_W, CELL_H = 48, 48

SCALE = 12
REPEAT = 5
FRAME_TIME = 0.1
PAUSE_TIME = 1.0

PLAY_ORDER = ['walk', 'jump', 'attack1', 'attack2', 'attack3']

FRAMES = {
    'walk': [
        (2, 44, 20, 31, 12, 10),
        (113, 110, 19, 28, 12, 10),
        (50, 110, 18, 29, 13, 9),
        (70, 110, 18, 29, 13, 9),
        (24, 44, 20, 31, 12, 10),
        (200, 77, 21, 30, 11, 10),
        (46, 44, 22, 31, 11, 9),
        (70, 44, 22, 31, 11, 9),
    ],
    'jump': [
        (94, 44, 20, 31, 12, 10),
        (90, 110, 21, 29, 11, 10),
        (223, 77, 22, 30, 11, 9),
        (2, 110, 22, 30, 11, 8),
        (26, 110, 22, 30, 11, 8),
    ],
    'attack1': [
        (116, 44, 20, 31, 12, 11),
        (198, 2, 20, 32, 12, 10),
        (2, 2, 44, 40, 4, 7),
        (75, 2, 30, 36, 17, 7),
        (107, 2, 30, 36, 17, 7),
        (138, 44, 20, 31, 12, 11),
    ],
    'attack2': [
        (160, 44, 20, 31, 12, 10),
        (182, 44, 16, 31, 14, 7),
        (200, 44, 16, 31, 14, 4),
        (139, 2, 18, 33, 16, 10),
        (48, 2, 25, 37, 16, 6),
        (159, 2, 37, 33, 11, 12),
    ],
    'attack3': [
        (218, 44, 20, 31, 12, 10),
        (134, 110, 18, 28, 13, 10),
        (174, 110, 32, 27, 7, 10),
        (208, 110, 35, 27, 5, 10),
        (154, 110, 18, 28, 13, 10),
    ],
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
running = True


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False


def wait(seconds):
    start = get_time()
    while running and get_time() - start < seconds:
        handle_events()
        delay(0.01)


def draw_frame(sheet, frame):
    fx, fy, fw, fh, ox, oy = frame

    dx = ox + fw / 2 - CELL_W / 2
    dy = oy + fh / 2 - CELL_H / 2

    x = CANVAS_W // 2 + dx * SCALE
    y = CANVAS_H // 2 - dy * SCALE

    bottom = SHEET_H - fy - fh

    clear_canvas()
    sheet.clip_draw(fx, bottom, fw, fh, x, y, fw * SCALE, fh * SCALE)
    update_canvas()


def play_animation(sheet, name):
    for _ in range(REPEAT):
        for frame in FRAMES[name]:
            if not running:
                return
            draw_frame(sheet, frame)
            wait(FRAME_TIME)

    wait(PAUSE_TIME)


open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image(os.path.join(BASE_DIR, SHEET_FILE))

while running:
    for name in PLAY_ORDER:
        if not running:
            break
        play_animation(sheet, name)

close_canvas()
