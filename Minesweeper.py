import pygame
import MinesweeperClass

msg = MinesweeperClass.MinesweeperGrid(10,10,5)
msg.setUpGame(1,1)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
MARGIN = 0

# unecessary right now
# mine = pygame.image.load('Minesweeper Images\\bomb.png')
# mine = pygame.transform.scale(mine,(WIDTH,HEIGHT))

#dictionary
tilePicDic = {}

tilePicDic['flagged'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\flagged.png'),(WIDTH,HEIGHT))
tilePicDic['covered'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\facingDown.png'),(WIDTH,HEIGHT))
tilePicDic['0'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\0.png'),(WIDTH,HEIGHT))
tilePicDic['1'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\1.png'),(WIDTH,HEIGHT))
tilePicDic['2'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\2.png'),(WIDTH,HEIGHT))
tilePicDic['3'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\3.png'),(WIDTH,HEIGHT))
tilePicDic['4'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\4.png'),(WIDTH,HEIGHT))
tilePicDic['5'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\5.png'),(WIDTH,HEIGHT))
tilePicDic['6'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\6.png'),(WIDTH,HEIGHT))
tilePicDic['7'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\7.png'),(WIDTH,HEIGHT))
tilePicDic['8'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\8.png'),(WIDTH,HEIGHT))
tilePicDic['mine'] = pygame.transform.scale(pygame.image.load('Minesweeper Images\\bomb.png'),(WIDTH,HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
screenWidth = (WIDTH + MARGIN) * msg.cols + MARGIN
screenHeight = (HEIGHT + MARGIN) * msg.rows + MARGIN
WINDOW_SIZE = [screenWidth, screenHeight]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and not msg.fail:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            print(pygame.mouse.get_pressed())
            if pygame.mouse.get_pressed() == (1, 0, 0):
                msg.openTile(row,column)
            elif pygame.mouse.get_pressed() == (0, 0, 1):
                msg.flagTile(row,column)
            elif pygame.mouse.get_pressed() == (1, 0, 1):
                msg.openAllNeighborTiles(row,column)

    # Set the screen background
    screen.fill(RED)

    # Draw the grid
    for row in range(msg.rows):
        for column in range(msg.cols):
            screen.blit(tilePicDic[msg.grid[row][column].key()],((MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN))

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

