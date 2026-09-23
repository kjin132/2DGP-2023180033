# 실습 과제 진행

from pico2d import *
open_canvas(800, 600)

character = load_image("character.png")


def move_Circle():
    print("circle")
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