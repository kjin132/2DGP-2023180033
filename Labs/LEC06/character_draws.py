# 실습 과제 진행

from pico2d import *
import math
open_canvas(800, 600)

character = load_image("character.png")

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.005)

def move_Circle():
    center_x, center_y = 400, 300
    radius = 150
    angle = 0
    speed = 2

    while angle < math.radians(360):
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        angle += math.radians(speed)
        draw_character(x, y)

def move_top():
    for x in range(50, 750, 5):
        draw_character(x, 550)
    
def move_right():
    for y in range(550, 50, -5):
        draw_character(750, y)

def move_bottom():
    for x in range(750, 50, -5):
        draw_character(x, 50)

def move_left():
    for y in range(50, 550, 5):
        draw_character(50, y)

def move_Rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_Triangle():
    points = [(400, 500), (200, 150), (600, 150)]
    speed = 5

    x, y = points[0]
    idx = 0
    count = 0

    while count < 3:
        target_x, target_y = points[(idx + 1) % 3]

        dx, dy = target_x - x, target_y - y
        dist = math.hypot(dx, dy)

        if dist < speed:
            idx = (idx + 1) % 3
            count += 1
        else:
            x += speed * dx / dist
            y += speed * dy / dist

        draw_character(x, y)

while True:
    move_Circle()
    move_Rectangle()
    move_Triangle()
    pass

close_canvas()