import pygame

from typing import Optional, Tuple
from src.entities.imagesprite import ImageSprite

class Explosion(ImageSprite):
    containers: Optional[Tuple[pygame.sprite.Group, ...]] = None
    explosion_frames: list[pygame.Surface] = []
    
    def __init__(self, position: pygame.Vector2, radius: float):
        if not Explosion.explosion_frames:
            explosion_sheet = pygame.image.load("assets/environment/asteroids/explode.png").convert_alpha()
            frame_width,frame_height = 96, 96  # TODO: hardcoded
            for frame in range(explosion_sheet.get_width() // frame_width):
                rect = pygame.Rect(frame * frame_width, 0, frame_width, frame_height)
                explosion_frame = explosion_sheet.subsurface(rect).copy()
                Explosion.explosion_frames.append(explosion_frame)
        
        super().__init__(position, Explosion.explosion_frames[1])
        self.current_frame = 1
        self.frame_duration = 0.1  # seconds per frame
        self.time_accumulator = 0.0
        self.radius = radius
        self.image = pygame.transform.scale(Explosion.explosion_frames[1],
                                            (int(radius * 5), int(radius * 5))) # TODO: hardcoded
        self.rect = self.image.get_rect(center=position)
        
    def update(self, dt: float):
        self.time_accumulator += dt
        if self.time_accumulator >= self.frame_duration:
            self.time_accumulator -= self.frame_duration
            self.current_frame += 1
            if self.current_frame < len(Explosion.explosion_frames) - 1:
                self.image = pygame.transform.scale(Explosion.explosion_frames[self.current_frame],
                                                    (int(self.radius * 5), int(self.radius * 5))) # TODO: hardcoded
                self.rect = self.image.get_rect(center=self.rect.center)
            else:
                self.kill()