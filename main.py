# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
clock = pygame.time.Clock()
dt = 0
from constants import *
from player import *

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	player = Player(x, y)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		dt = clock.tick(60)/1000

		screen.fill("black")
		player.update(dt)
		player.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
    main()
