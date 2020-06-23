import sys
import pygame

def check_keydown_events(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_UP:
        nave.moving_up = True
    elif event.key == pygame.K_DOWN:
        nave.moving_down = True


def check_keyup_events(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False
    elif event.key == pygame.K_UP:
        nave.moving_up = False
    elif event.key == pygame.K_DOWN:
        nave.moving_down = False


def check_events(nave):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, nave)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, nave)

def update_screen(image, screen, nave):
    screen.blit(image, (0, 0))
    nave.blitme()
    pygame.display.flip()
