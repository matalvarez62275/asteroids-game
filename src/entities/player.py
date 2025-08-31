import pygame

from src.entities.shot import Shot
from src.entities.circleshape import CircleShape
from src.settings import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, position: pygame.Vector2):
        
        super().__init__(position, PLAYER_RADIUS)
        
        self.lives = 3
        self.rotation = 180
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "skyblue", self.triangle(), 2)
        
    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def update(self, dt: float):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown < 0:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN
            
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        nose = self.position + forward * self.radius
        shot = Shot(nose)   # type: ignore
        shot.velocity = forward * PLAYER_SHOOT_SPEED