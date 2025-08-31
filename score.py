import pygame
from typing import Optional, Tuple

class Score(pygame.sprite.Sprite):
    containers: Optional[Tuple[pygame.sprite.Group, ...]] = None

    def __init__(self):
        if self.containers is not None:
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.points = 0

    def add_points(self, points: int) -> None:
        self.points += points

    def draw(self, screen: pygame.Surface) -> None:
        score_text = self.font.render(f"Score: {self.points}", True, "green")
        screen.blit(score_text, (10, 10))