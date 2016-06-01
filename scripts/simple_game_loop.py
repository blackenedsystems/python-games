import pygame

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

	# Some game logic ....

	clock.tick(fps)