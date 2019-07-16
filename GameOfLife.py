import pygame
import GameOfLifeClass

rows = 80
cols = 120
gol = GameOfLifeClass.gameoflifegrid(rows,cols)
gol.makeGliderGun()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(WIDTH + MARGIN) * rows + MARGIN, (HEIGHT + MARGIN) * rows + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
keepGoing = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            keepGoing = False
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if gol.grid[row][column] == 1:
                gol.grid[row][column] = 0
                print("self.grid[" + str(row) + "][" + str(column) + "] = 0")
            else:
                gol.grid[row][column] = 1
                print("self.grid[" + str(row) + "][" + str(column) + "] = 1")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                keepGoing = False
                gol.nextstep()
            if event.key == pygame.K_SPACE:
                keepGoing = True

    if keepGoing:
        gol.nextstep()
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(rows):
        for column in range(cols):
            color = WHITE
            if gol.grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

# if alive - two or three live neighbors - stays alive
# if exactly 3 neighbors, dead becomes alive
