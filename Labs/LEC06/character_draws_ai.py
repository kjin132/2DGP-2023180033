# 실습 과제 진행: 캐릭터 원운동 / 사각운동 / 삼각운동 무한 반복

from pico2d import *
import math

CANVAS_W, CANVAS_H = 800, 600

open_canvas(CANVAS_W, CANVAS_H)
character = load_image('character.png')

running = True


def process_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False


def draw_at(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()


def move_along_path(points, speed, frame_delay=0.01):
    """points를 순서대로 잇는 폐곡선을 따라 한 바퀴 이동한다."""
    n = len(points)
    x, y = points[0]

    for i in range(n):
        if not running:
            return
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        steps = max(1, round(dist / speed))
        step_x, step_y = dx / steps, dy / steps

        for _ in range(steps):
            if not running:
                return
            x += step_x
            y += step_y
            draw_at(x, y)
            delay(frame_delay)
            process_events()


def move_circle(center=(400, 300), radius=150, speed_deg=2, frame_delay=0.005):
    cx, cy = center
    angle = 0.0
    while running and angle < 360:
        x = cx + radius * math.cos(math.radians(angle))
        y = cy + radius * math.sin(math.radians(angle))
        draw_at(x, y)
        delay(frame_delay)
        process_events()
        angle += speed_deg


def move_rectangle():
    corners = [(50, 550), (750, 550), (750, 50), (50, 50)]
    move_along_path(corners, speed=8)


def move_triangle():
    corners = [(400, 500), (200, 150), (600, 150)]
    move_along_path(corners, speed=5)


def main():
    motions = [move_circle, move_rectangle, move_triangle]
    while running:
        for motion in motions:
            if not running:
                break
            motion()
    close_canvas()


main()