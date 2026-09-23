# 실습 과제 진행

from pico2d import *
import math
open_canvas(800, 600)

character = load_image("character.png")

def move_Circle():
    print("circle")

    center_x, center_y = 400, 300
    radius = 150
    angle = 0
    speed = 2

    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    clear_canvas()
    character.draw(400, 300)
    update_canvas()

def move_Rectangle():
    print("rectangle")

def move_Triangle():
    print("triangle")

while True:
    move_Circle()
    move_Rectangle()
    move_Triangle()
    pass

close_canvas()