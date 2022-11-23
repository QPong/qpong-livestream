from utils.parameters import WINDOW_WIDTH, WIDTH_UNIT
from utils.colors import GRAY
from utils.font import Font

def draw_score(score1, score2, screen):

    font = Font()

    # Print the score
    text = font.player_font.render("Classical Computer", 1, GRAY)
    text_pos = text.get_rect(
        center=(round(WINDOW_WIDTH * 0.25) + WIDTH_UNIT * 4.5, WIDTH_UNIT * 1.5)
    )
    screen.blit(text, text_pos)

    text = font.player_font.render("Quantum Computer", 1, GRAY)
    text_pos = text.get_rect(
        center=(round(WINDOW_WIDTH * 0.75) - WIDTH_UNIT * 4.5, WIDTH_UNIT * 1.5)
    )
    screen.blit(text, text_pos)

    text = font.score_font.render(str(score1), 1, GRAY)
    text_pos = text.get_rect(
        center=(round(WINDOW_WIDTH * 0.25) + WIDTH_UNIT * 4.5, WIDTH_UNIT * 8)
    )
    screen.blit(text, text_pos)

    text = font.score_font.render(str(score2), 1, GRAY)
    text_pos = text.get_rect(
        center=(round(WINDOW_WIDTH * 0.75) - WIDTH_UNIT * 4.5, WIDTH_UNIT * 8)
    )
    screen.blit(text, text_pos)
