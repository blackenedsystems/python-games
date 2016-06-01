import pygame

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
	# Initialise pygame
	pygame.init()

	# The window in which the game will run...
	size = (700, 500)
	screen = pygame.display.set_mode(size)
	
	pygame.display.set_caption("Simple Game Loop")

	# Loop until the user clicks the close button.
	done = False

	# Manages screen refresh rate
	clock = pygame.time.Clock()
	fps = 60

	while not done:	
		# Main event loop...
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # User pressed close, so end the script.
				done = True

		# Clear the screen
		screen.fill(WHITE)

		# Draw stuff / Game Logic ...

		# Update the screen
		pygame.display.flip()

		# Limit to fps frames per second
		clock.tick(fps)

if __name__ == "__main__":
	main()		