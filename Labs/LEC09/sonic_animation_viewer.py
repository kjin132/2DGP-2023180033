from pico2d import *
import os

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SPRITE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sonic-sprite.png")
SPRITE_HEIGHT = 525
SCALE = 8
REPEAT_COUNT = 5
PAUSE_TIME = 1.0
FLOOR_Y = 130
START_X = 180
END_X = CANVAS_WIDTH - 180
CENTER_X = CANVAS_WIDTH / 2


def handle_events():
	for event in get_events():
		if event.type == SDL_QUIT:
			return False
		if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			return False
	return True


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	sprite_sheet = load_image(SPRITE_PATH)
	running = True
	while running:
		running = handle_events()
		if not running:
			break
		clear_canvas()
		update_canvas()
		delay(0.01)
	close_canvas()


if __name__ == "__main__":
	main()
