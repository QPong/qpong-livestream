import pygame

from .resources import Font
from . import parameters
from . import colors


def draw_statevector_grid(screen):
    font = Font()
    basis_states = [
        '|000>',
        '|001>',
        '|010>',
        '|011>',
        '|100>',
        '|101>',
        '|110>',
        '|111>'
    ]
    block_size = int(round(parameters.SCREEN_HEIGHT / len(basis_states)))

    for i in range(len(basis_states)):
        text = font.vector_font.render(basis_states[i], 1, colors.WHITE)
        screen.blit(text, (parameters.WINDOW_WIDTH - text.get_width(), 
                            i*block_size + text.get_height()))


def draw_score(score1, score2, screen):
    font = Font()
    
    text = font.player_font.render("Classical Computer", 1, colors.GRAY)
    text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH*0.3, parameters.WIDTH_UNIT*2))
    screen.blit(text, text_pos)
    
    text = font.score_font.render(str(score1), 1, colors.GRAY)
    text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH*0.3, parameters.WIDTH_UNIT*8))
    screen.blit(text, text_pos)
    
    text = font.player_font.render("Quantum Computer", 1, colors.GRAY)
    text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH*0.7, parameters.WIDTH_UNIT*2))
    screen.blit(text, text_pos)
    
    text = font.score_font.render(str(score2), 1, colors.GRAY)
    text_pos = text.get_rect(center=(parameters.WINDOW_WIDTH*0.7, parameters.WIDTH_UNIT*8))
    screen.blit(text, text_pos)


def draw_dashed_line(screen):
    for i in range(10, parameters.SCREEN_HEIGHT, 2 * parameters.WIDTH_UNIT): 
        pygame.draw.rect(
            screen,
            colors.GRAY,
            (parameters.WINDOW_WIDTH // 2 - 5, i, 0.5 * parameters.WIDTH_UNIT, parameters.WIDTH_UNIT),
            0,
        )
