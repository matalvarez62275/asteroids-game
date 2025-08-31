import pygame
from src.core.game import Game
from src.entities.shot import Shot
from src.entities.score import Score
from src.entities.player import Player
from src.entities.asteroid import Asteroid
from src.entities.asteroidfield import AsteroidField
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

    game = Game(player, asteroid_field, score, heart_img, updatable, drawable, asteroids, shots)
    game.run()

if __name__ == "__main__":
    main()