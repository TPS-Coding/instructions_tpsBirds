from settings import *
from background import BG
from player import Player
from obs import Obstacle
from timer import Timer


class Game():
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("TPS Birds")

        self.clock = pygame.time.Clock()
        self.running = True
        self.lives = 3
        self.hit_timer = Timer(1500)
        self.spawn_timer = Timer(2000)

        ## groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        ## sprites
        
        BG(self.all_sprites)
        self.player = Player(self.all_sprites)
        

    def check_collisions(self):
        for sprite in self.collision_sprites:
            if pygame.sprite.collide_rect(self.player, sprite) and not self.hit_timer.active:
                self.lives -= 1
                self.hit_timer.activate()
                print(self.lives)


    def spawn_obstacles(self):
        self.spawn_timer.activate()
        direction = choice(["up", "down"]) ## this will randomly choose between up and down
        print(direction)
        if direction == 'up':
            pos = (WINDOW_WIDTH + 50, WINDOW_HEIGHT - 50)
        else:
            pos = (WINDOW_WIDTH + 50, 0+50)
        Obstacle((self.all_sprites, self.collision_sprites), pos, direction)

        



    def run(self):
        dt = 0.08
        while self.running:

            self.clock.tick(FRAMERATE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            if not self.spawn_timer.active:
                self.spawn_obstacles()


            ## draw
            self.display_surface.fill('purple')
            self.all_sprites.draw(self.display_surface)


            ### update
            self.hit_timer.update()
            self.spawn_timer.update()
            self.all_sprites.update(dt)
            self.check_collisions()
            pygame.display.update()
            

            self.clock.tick(120)




if __name__ == '__main__':
    game = Game()
    game.run()
