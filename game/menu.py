import sys
import pygame
import pygame_gui
from .constants import *

def settings():
    pass

def return_score_board():
    pass

def update_score_board():
    # Datetime
    # Name
    # In top 10?
    # Sort in top 10
    pass

def menu_loop(screen, background_image, font):
    # TODO: Use update_score_board
    # update_score_board(score, name)
    
    play_rect = pygame.Rect(
            (SCREEN_WIDTH/4, SCREEN_HEIGHT/4.5, 
             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
            )
    play_text = font.render('Play (or Space)', True, (0,255,0))
    play_text_rect = play_text.get_rect(center=play_rect.center)

    score_rect = pygame.Rect(
            (SCREEN_WIDTH/4, SCREEN_HEIGHT/4.5*2, 
             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
            )
    score_text = font.render('Score Board', True, (0,255,0))
    score_text_rect = score_text.get_rect(center=score_rect.center)

    settings_rect = pygame.Rect(
            (SCREEN_WIDTH/4, SCREEN_HEIGHT/4.5*3, 
             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
            )
    settings_text = font.render('Lives', True, (0,255,0))
    settings_text_rect = settings_text.get_rect(center=settings_rect.center)


    # TODO: create the menu display and go to the game

    menu_running = True
    clock = pygame.time.Clock()

    while menu_running:
        time_delta = clock.tick(60)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print("Clicked")
                state = "game"
                menu_running = False
                return state

        screen.fill((0,0,0))
        screen.blit(background_image, (0,0))
        pygame.draw.rect(screen, (255,255,255), play_rect, 2)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, (255,255,255), score_rect, 2)
        screen.blit(score_text, score_text_rect)
        pygame.draw.rect(screen, (255,255,255), settings_rect, 2)
        screen.blit(settings_text, settings_text_rect)
        pygame.display.update()