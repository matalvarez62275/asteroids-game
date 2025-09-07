import pygame

from src.entities.shot import Shot
from src.entities.heart import Heart
from src.entities.player import Player
from src.entities.asteroid import Asteroid
from src.entities.explosion import Explosion
from src.entities.asteroidfield import AsteroidField
from src.core.events import handle_player_input
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, FPS, FONT_SIZE_REGULAR, FONT_SIZE_LARGE

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.font_regular = pygame.font.Font("assets/fonts/dogica.ttf", FONT_SIZE_REGULAR)
        self.font_large_bold = pygame.font.Font("assets/fonts/dogicabold.ttf", FONT_SIZE_LARGE)
        
        # Sprite groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.LayeredUpdates()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        # Set containers for sprite classes
        AsteroidField.containers = (self.updatable, )
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        Explosion.containers = (self.updatable, self.drawable)
        Player.containers = (self.updatable, self.drawable)
        Heart.containers = (self.drawable, )
        Shot.containers = (self.shots, self.updatable, self.drawable)

        # Create game objects
        self.asteroid_field = AsteroidField()
        self.player = Player()
        self.score = 0
        
        self.hearts = [
            Heart(pygame.Vector2(SCREEN_WIDTH - 40 - i * 40, 25))
            for i in range(self.player.lives)
        ]
        for heart in self.hearts:
            self.drawable.add(heart)
        
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
                    if self.hearts:
                        lost_heart = self.hearts.pop()
                        lost_heart.kill()
                    if self.player.lives <= 0:
                        self.player.kill()
                        break
                        
            for shot in self.shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    match asteroid.radius / ASTEROID_MIN_RADIUS:
                        case 1:
                            self.score += 15
                        case 2:
                            self.score += 10
                        case 3:
                            self.score += 5
                    break

        # Handle restart
        keys = pygame.key.get_pressed()
        if self.player.lives <= 0 and keys[pygame.K_r]:
            self.player = Player(pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            self.score = 0
            for asteroid in self.asteroids:
                asteroid.kill()
            for shot in self.shots:
                shot.kill()
            
            # Restore hearts
            self.hearts.clear()
            for i in range(self.player.lives):
                heart = Heart(pygame.Vector2(SCREEN_WIDTH - 40 - i * 40, 25))
                self.hearts.append(heart)

    def draw(self):
        self.screen.fill("black")
        
        if self.player.lives > 0:
            
            # All drawable sprites MUST have an 'image' attribute and a 'rect' attribute
            self.drawable.draw(self.screen)
            
            for i, heart in enumerate(self.hearts):
                heart.visible = i < self.player.lives 
                
            score_text = self.font_regular.render(f"Score: {self.score}", True, "green")
            self.screen.blit(score_text, (10, 10))
            
        else:
            game_over_text = self.font_large_bold.render("G A M E  O V E R", True, "red")
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 170))
            
            restart_text = self.font_regular.render("Press  R  to restart", True, "white")
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
            
            score_text = self.font_regular.render(f"Score: {self.score}", True, "green")
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
            
            self.screen.blits([(game_over_text, game_over_rect),
                               (restart_text, restart_rect),
                               (score_text, score_rect)])
            
        pygame.display.flip()