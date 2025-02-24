# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
clock = pygame.time.Clock()
dt = 0
from constants import *
from player import *
from asteroidfield import *

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(x, y)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		dt = clock.tick(60)/1000

		screen.fill("black")
		updatable.update(dt)
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()

		for asteroid in asteroids:
			if player.is_collision(asteroid):
				print("Game over!")
				raise SystemExit

if __name__ == "__main__":
    main()
