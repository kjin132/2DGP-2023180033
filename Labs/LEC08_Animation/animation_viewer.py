import os

from pico2d import *

SHEET_FILE = 'warrior_sheet.png'
SHEET_W, SHEET_H = 256, 171

SCALE = 12

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def draw_frame(sheet, frame):
    fx, fy, fw, fh = frame
    bottom = SHEET_H - fy - fh

    clear_canvas()
    sheet.clip_draw(fx, bottom, fw, fh, 400, 300, fw * SCALE, fh * SCALE)
    update_canvas()


open_canvas(800, 600)

sheet = load_image(os.path.join(BASE_DIR, SHEET_FILE))

draw_frame(sheet, (2, 44, 20, 31))

delay(2)

close_canvas()
