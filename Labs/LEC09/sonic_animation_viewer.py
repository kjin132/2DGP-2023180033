from pico2d import *
import os

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SPRITE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sonic-sprite.png")


def handle_events():
	for event in get_events():
		if event.type == SDL_QUIT:
			return False
		if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			return False
	return True


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	close_canvas()


if __name__ == "__main__":
	main()
