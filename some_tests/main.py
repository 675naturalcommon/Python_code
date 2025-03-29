import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plants vs Zombies")

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.shoot_timer = 0

    def update(self):
        self.shoot_timer += 1
        if self.shoot_timer > 60:  # Shoot every second
            self.shoot_timer = 0
            return True
        return False

class Zombie(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = y
        self.speed = 1
        self.health = 100

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -50:
            self.kill()

class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_WIDTH:
            self.kill()

def main():
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    plants = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    peas = pygame.sprite.Group()

    # Create initial plants
    for i in range(5):
        plant = Plant(100, 100 + i * 100)
        plants.add(plant)
        all_sprites.add(plant)

    # Game loop
    running = True
    zombie_spawn_timer = 0
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spawn zombies
        zombie_spawn_timer += 1
        if zombie_spawn_timer > 120:  # Every 2 seconds
            zombie_spawn_timer = 0
            zombie = Zombie(random.choice([100, 200, 300, 400, 500]))
            zombies.add(zombie)
            all_sprites.add(zombie)

        # Update game objects
        all_sprites.update()

        # Plants shooting
        for plant in plants:
            if plant.update():
                pea = Pea(plant.rect.x + 50, plant.rect.y + 20)
                peas.add(pea)
                all_sprites.add(pea)

        # Collision detection
        for pea in peas:
            zombie_hit = pygame.sprite.spritecollideany(pea, zombies)
            if zombie_hit:
                zombie_hit.health -= 10
                if zombie_hit.health <= 0:
                    zombie_hit.kill()
                pea.kill()

        # Draw everything
        screen.fill((0, 100, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
