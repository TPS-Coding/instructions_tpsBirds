from settings import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,groups, pos, direction):
        super().__init__(groups)

        self.direction = direction
        self.image = pygame.image.load("../graphics/backgrounds/Obstacle2.png")
        if self.direction == "down":
            self.image = pygame.transform.rotate(self.image, 180)
            
        self.rect = self.image.get_frect(center = pos)

        self.direction = -1
        self.speed = 50

    def move(self, dt):
        self.rect.x += self.direction * self.speed * dt
        if self.rect.right <= 0:
            self.kill()

    def update(self,dt):
        self.move(dt)

