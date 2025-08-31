import pygame

from src.entities.shot import Shot
from src.entities.circleshape import CircleShape
from src.settings import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_STARTING_LIVES, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(CircleShape):
    player_image: pygame.Surface = None  # type: ignore
    
    def __init__(self, position: pygame.Vector2 = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)):
        super().__init__(position, PLAYER_RADIUS)
        
        if Player.player_image is None:
            player_image = pygame.image.load("assets/ship.png").convert_alpha()
            Player.player_image = pygame.transform.scale(player_image,
                                                         (PLAYER_RADIUS * 4, PLAYER_RADIUS * 4))    # TODO: remove hardocoding
            
        self.image = Player.player_image
        self.rect = self.image.get_rect(center=position)
        
        self.lives = PLAYER_STARTING_LIVES
        self.rotation = 180
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.image = pygame.transform.rotate(Player.player_image, 180 - self.rotation)
        self.rect = self.image.get_rect(center=self.position)
        
    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = self.position  # type: ignore
        
    def update(self, dt: float):
        self.cooldown -= dt
            
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position + forward * self.radius, self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED