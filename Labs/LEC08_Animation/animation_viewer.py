import os

from pico2d import *

SHEET_FILE = 'warrior_sheet.png'
SHEET_W, SHEET_H = 256, 171

SCALE = 12
FRAME_TIME = 0.1

FRAMES = {
    'walk': [
        (2, 44, 20, 31),
        (113, 110, 19, 28),
        (50, 110, 18, 29),
        (70, 110, 18, 29),
        (24, 44, 20, 31),
        (200, 77, 21, 30),
        (46, 44, 22, 31),
        (70, 44, 22, 31),
    ],
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def draw_frame(sheet, frame):
    fx, fy, fw, fh = frame
    bottom = SHEET_H - fy - fh

    clear_canvas()
    sheet.clip_draw(fx, bottom, fw, fh, 400, 300, fw * SCALE, fh * SCALE)
    update_canvas()


open_canvas(800, 600)

sheet = load_image(os.path.join(BASE_DIR, SHEET_FILE))

for frame in FRAMES['walk']:
    draw_frame(sheet, frame)
    delay(FRAME_TIME)

delay(1)

close_canvas()
