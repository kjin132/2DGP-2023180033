import os

from pico2d import *

SHEET_FILE = 'warrior_sheet.png'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


open_canvas(800, 600)

sheet = load_image(os.path.join(BASE_DIR, SHEET_FILE))

delay(2)

close_canvas()
