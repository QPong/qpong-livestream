from utils.parameters import WINDOW_WIDTH, WIDTH_UNIT, NUM_QUBITS, SCREEN_HEIGHT
from utils.colors import GRAY, WHITE
from utils.font import Font
from utils.states import comp_basis_states

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


def draw_statevector_grid(screen):
    font = Font()
    block_size = int(round(SCREEN_HEIGHT / 2**NUM_QUBITS))
    basis_states = comp_basis_states(NUM_QUBITS)

    for qb_idx in range(2**NUM_QUBITS):
        text = font.vector_font.render(
            "|" + basis_states[qb_idx] + ">", 1, WHITE
        )
        text_height = text.get_height()
        y_offset = block_size * 0.5 - text_height * 0.5
        screen.blit(text, (WINDOW_WIDTH - 7*WIDTH_UNIT, qb_idx * block_size + y_offset))
