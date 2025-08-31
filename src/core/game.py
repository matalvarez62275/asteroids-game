import pygame
from src.core.events import handle_player_input
from src.entities.textdisplayable import TextDisplayable
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, FPS

class Game:
    def __init__(self, player, asteroid_field, score, heart_img, updatable, drawable, asteroids, shots):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = player
        self.asteroid_field = asteroid_field
        self.score = score
        self.heart_img = heart_img
        self.updatable = updatable
        self.drawable = drawable
        self.asteroids = asteroids
        self.shots = shots
        self.running = True

    def run(self):
        dt = 0
        while self.running:
            self.handle_events()
            self.update(dt)
            self.draw()
            dt = self.clock.tick(FPS) / 1000

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        handle_player_input(self.player, dt)
        self.updatable.update(dt)
        
        for asteroid in self.asteroids:
            if asteroid.collides_with(self.player):
                if self.player.lives > 0:
                    self.player.lives -= 1
                    asteroid.split()
            for shot in self.shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    match asteroid.radius / ASTEROID_MIN_RADIUS:
                        case 1:
                            self.score.add_points(15)
                        case 2:
                            self.score.add_points(10)
                        case 3:
                            self.score.add_points(5)
                    break

        # Handle restart
        keys = pygame.key.get_pressed()
        if self.player.lives <= 0 and keys[pygame.K_r]:
            self.player.lives = 3
            self.player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            self.player.rotation = 180
            self.score.points = 0
            for asteroid in self.asteroids:
                asteroid.kill()
            for shot in self.shots:
                shot.kill()

    def draw(self):
        self.screen.fill("black")
        if self.player.lives > 0:
            for sprite in self.drawable:
                sprite.draw(self.screen)
            for i in range(self.player.lives):
                life_rect = self.heart_img.get_rect(center=(SCREEN_WIDTH - 40 - i * 40, 25))
                self.screen.blit(self.heart_img, life_rect)
        else:
            game_over_text = TextDisplayable("GAME OVER", font_size=72, color="red")
            game_over_text.draw(self.screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100), center=True)
            restart_text = TextDisplayable("Press R to Restart", font_size=36, color="yellow")
            restart_text.draw(self.screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50), center=True)
            self.score.draw(self.screen)
        pygame.display.flip()