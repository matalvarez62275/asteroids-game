import sys
import pygame
from pygame import Vector2

from src.entities.shot import Shot
from src.entities.score import Score
from src.entities.player import Player
from src.entities.asteroid import Asteroid
from src.entities.imagesprite import ImageSprite
from src.entities.asteroidfield import AsteroidField
from src.entities.textdisplayable import TextDisplayable 
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ASTEROID_MIN_RADIUS

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    
    Score.containers = (drawable, )
    score = Score()
    
    heart_img = pygame.image.load("assets/heart.png").convert_alpha()
    heart_img = pygame.transform.scale(heart_img, (40, 40)) 
    
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if player.lives > 0:
                    player.lives -= 1
                    asteroid.split()
                         
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    match asteroid.radius/ASTEROID_MIN_RADIUS:
                        case 1:
                            score.add_points(15)
                        case 2:
                            score.add_points(10)
                        case 3:
                            score.add_points(5)
                    break
                
        screen.fill("black")
            
        if player.lives > 0:
            for sprite in drawable:
                sprite.draw(screen)
            for i in range(player.lives):
                life_rect = heart_img.get_rect(center=(SCREEN_WIDTH - 40 - i * 40, 25))
                screen.blit(heart_img, life_rect) 
        else:
            game_over_text = TextDisplayable("GAME OVER", font_size=72, color="red")
            game_over_text.draw(screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100), center = True)
            restart_text = TextDisplayable("Press R to Restart", font_size=36, color="yellow")
            restart_text.draw(screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50), center = True)
            score.draw(screen)
            if  pygame.key.get_pressed()[pygame.K_r]:
                player.lives = 3
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                player.rotation = 180
                score.points = 0
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()
                
        
        pygame.display.flip()
        
        dt = clock.tick(FPS)/1000

if __name__ == "__main__":
    main()