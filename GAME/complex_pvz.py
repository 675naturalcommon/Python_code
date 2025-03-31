import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRID_SIZE = 80
GRID_WIDTH = 9
GRID_HEIGHT = 5
LAWN_LEFT = 100
LAWN_TOP = 100

# 颜色定义
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("复杂版植物大战僵尸")
clock = pygame.time.Clock()

class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.attack_power = 10
        self.cooldown = 0
        self.max_cooldown = 30

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, GREEN,
                          (self.x + GRID_SIZE//2, self.y + GRID_SIZE//2),
                          GRID_SIZE//3)

    def can_attack(self):
        return self.cooldown == 0

    def attack(self, zombies):
        if self.can_attack():
            for zombie in zombies:
                if zombie.row == self.y // GRID_SIZE:
                    zombie.health -= self.attack_power
                    self.cooldown = self.max_cooldown
                    return True
        return False

class Zombie:
    def __init__(self, row):
        self.x = SCREEN_WIDTH
        self.row = row
        self.y = LAWN_TOP + row * GRID_SIZE
        self.health = 50
        self.speed = 1
        self.damage = 0.5

    def update(self):
        self.x -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN,
                        (self.x, self.y, GRID_SIZE//2, GRID_SIZE))

    def attack_plant(self, plants):
        for plant in plants:
            if (plant.y // GRID_SIZE == self.row and
                abs(plant.x - self.x) < GRID_SIZE):
                plant.health -= self.damage
                return True
        return False

class Game:
    def __init__(self):
        self.plants = []
        self.zombies = []
        self.sun = 50
        self.spawn_timer = 0
        self.game_over = False
        self.font = pygame.font.SysFont(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = (mouse_x - LAWN_LEFT) // GRID_SIZE
                grid_y = (mouse_y - LAWN_TOP) // GRID_SIZE

                if (0 <= grid_x < GRID_WIDTH and
                    0 <= grid_y < GRID_HEIGHT and
                    self.sun >= 25):
                    plant_x = LAWN_LEFT + grid_x * GRID_SIZE
                    plant_y = LAWN_TOP + grid_y * GRID_SIZE
                    self.plants.append(Plant(plant_x, plant_y))
                    self.sun -= 25

    def update(self):
        if self.game_over:
            return

        # 更新植物
        for plant in self.plants:
            plant.update()
            plant.attack(self.zombies)

        # 更新僵尸
        for zombie in self.zombies:
            zombie.update()
            zombie.attack_plant(self.plants)

        # 生成僵尸
        self.spawn_timer += 1
        if self.spawn_timer >= 180:  # 每3秒生成一个僵尸
            row = random.randint(0, GRID_HEIGHT-1)
            self.zombies.append(Zombie(row))
            self.spawn_timer = 0

        # 生成阳光
        if random.random() < 0.01:  # 1%几率每帧生成阳光
            self.sun += 5

        # 检查游戏结束条件
        for zombie in self.zombies:
            if zombie.x < 0:
                self.game_over = True

        # 移除死亡的植物和僵尸
        self.plants = [p for p in self.plants if p.health > 0]
        self.zombies = [z for z in self.zombies if z.health > 0]

    def draw(self):
        screen.fill(BLUE)  # 天空背景

        # 绘制草坪网格
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(
                    LAWN_LEFT + x * GRID_SIZE,
                    LAWN_TOP + y * GRID_SIZE,
                    GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, GREEN, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

        # 绘制植物和僵尸
        for plant in self.plants:
            plant.draw(screen)

        for zombie in self.zombies:
            zombie.draw(screen)

        # 绘制阳光数量
        sun_text = self.font.render(f"阳光: {self.sun}", True, WHITE)
        screen.blit(sun_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render("游戏结束!", True, WHITE)
            screen.blit(game_over_text,
                       (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
