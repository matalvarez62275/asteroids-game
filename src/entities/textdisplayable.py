import pygame

class TextDisplayable(pygame.font.Font):
    def __init__(self,
                 text: str, font_path: str | None = None,
                 font_size: int = 36,
                 color: str = "white",
                 background_color: str | None = None):
                 
        super().__init__(font_path, font_size)
        self.text = text
        self.color = color
        self.background_color = background_color
        
    def draw(self, screen: pygame.Surface, position: tuple[float, float], center: bool = False) -> None:
        text_surface = self.render(self.text, True, self.color, self.background_color)
        if center:
            display_rect = text_surface.get_rect(center=position)
            screen.blit(text_surface, display_rect)
        else:
            screen.blit(text_surface, position)