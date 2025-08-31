import pygame

from src.settings import PLAYER_SHOOT_COOLDOWN

def handle_player_input(player, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.rotate(-dt)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.rotate(dt)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move(-dt)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move(dt)
    if keys[pygame.K_SPACE]:
        if player.cooldown < 0:
            player.shoot()
            player.cooldown = PLAYER_SHOOT_COOLDOWN