import os

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
SHEET_FILE = 'warrior_sheet.png'
SHEET_W, SHEET_H = 256, 171
CELL_W, CELL_H = 48, 48

SCALE = 12
FRAME_TIME = 0.1

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
    for frame in FRAMES[name]:
        if not running:
            return
        draw_frame(sheet, frame)
        wait(FRAME_TIME)


open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image(os.path.join(BASE_DIR, SHEET_FILE))

play_animation(sheet, 'walk')

wait(1)

close_canvas()
