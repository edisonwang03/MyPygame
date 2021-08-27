import pygame, random

pygame.init()
pygame.display.set_caption("Galaga")

# Initialize variables
clock = pygame.time.Clock()
screen_Width = 600
screen_Height = 1000
surface = pygame.display.set_mode((screen_Width, screen_Height))
black = 0, 0, 0


# Classes for game objects
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Player, self).__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("D:\\code\\Python code\\Pygame\\Galaga Images\\player.png"), (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    # Moves the player left or right
    def move(self, direction):
        if direction == "S":
            self.rect.x -= 8
        if direction == "E":
            self.rect.x += 8

    # Draws the player onto the screen
    def draw(self):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("D:\\code\\Python code\\Pygame\\Galaga Images\\enemy.png"), (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    # Moves the enemy left or right
    def move(self, direction):
        if direction == "W":
            self.rect.x -= 1
        if direction == "E":
            self.rect.x += 1

    # Draws the enemy onto the screen
    def draw(self):
        surface.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Bullet, self).__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("D:\\code\\Python code\\Pygame\\Galaga Images\\bullet.png"), (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    # Moves the bullet up or down
    def move(self, direction):
        if direction == "N":
            self.rect.y -= 8
        if direction == "S":
            self.rect.y += 8

    # Returns whether the bullet has collided with another rect
    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    # Draws the enemy onto the screen
    def draw(self):
        surface.blit(self.image, self.rect)


# Initialize game objects
player = Player(375, 800, 40, 40)
playerBullets = []
enemyBullets = []
enemies = []
enemiesRows = 4
enemiesCols = 8
eX = 100
eY = 100
for i in range(enemiesRows):
    eY += 50
    eX = 100
    for j in range(enemiesCols):
        enemies.append(Enemy(eX, eY, 40, 40))
        eX += 50

# Main program loop
done = False
pressedLeft = False
pressedRight = False
movingRight = True
while not done:
    # Get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 97:  # a
                pressedLeft = True
            if event.key == 100:  # d
                pressedRight = True
            if event.key == 27:  # esc
                done = True
            if event.key == 32:  # spacebar
                # Player fires a bullet
                pbWidth = 8
                pbHeight = 24
                pbX = player.rect.x + (player.rect.width / 2) - (pbWidth / 2)
                pbY = player.rect.y - pbHeight
                pb = Bullet(pbX, pbY, pbWidth, pbHeight)
                playerBullets.append(pb)

        elif event.type == pygame.KEYUP:
            if event.key == 97:  # a
                pressedLeft = False
            if event.key == 100:  # d
                pressedRight = False

    # Update game objects
    # Allows player to hold keys to move left and right
    if pressedLeft and player.rect.x >= 8:
        player.move("S")
    if pressedRight and player.rect.x <= screen_Width - player.rect.width - 8:
        player.move("E")

    # Makes enemies shift left and right across the screen
    if movingRight:
        for e in enemies:
            e.move("E")
            if e.rect.x + e.rect.width >= screen_Width - 8:
                movingRight = False
    else:
        for e in enemies:
            e.move("W")
            if e.rect.x <= 8:
                movingRight = True

    # Moves player bullets up
    for pb in playerBullets:
        pb.move("N")

    # Removes player bullets when they go off the screen
    for i in reversed(range(len(playerBullets))):
        if playerBullets[i].rect.y <= 0 - playerBullets[i].rect.height:
            del playerBullets[i]
            break

    # Removes player bullets and enemies when the two collide
    for i in reversed(range(len(playerBullets))):
        for j in reversed(range(len(enemies))):
            if playerBullets[i].collided(enemies[j].rect):
                del playerBullets[i]
                del enemies[j]
                break

    # Randomly makes an enemy shoot a bullet
    for e in enemies:
        if random.randint(1, 800) == 400:  # 400 doesn't matter
            ebWidth = 8
            ebHeight = 24
            ebX = e.rect.x + (e.rect.width / 2) - (ebWidth / 2)
            ebY = e.rect.y + e.rect.height
            eb = Bullet(ebX, ebY, ebWidth, ebHeight)
            enemyBullets.append(eb)

    # Moves enemy bullets down
    for eb in enemyBullets:
        eb.move("S")

    # Removes enemy bullet if it collides with the player. Ends game in a loss
    for i in reversed(range(len(enemyBullets))):
        if enemyBullets[i].collided(player.rect):
            del enemyBullets[i]
            print("You lost...")
            done = True

    # Checks if all enemies have been defeated. Ends game in a win
    if len(enemies) == 0:
        print("You won!")
        done = True

    # Draw game objects
    pygame.display.flip()
    surface.fill(black)
    player.draw()
    for e in enemies:
        e.draw()
    for pb in playerBullets:
        pb.draw()
    for eb in enemyBullets:
        eb.draw()
    clock.tick(60)  # FPS
pygame.quit()
quit()
