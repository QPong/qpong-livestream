from utils.parameters import WINDOW_WIDTH, WIDTH_UNIT, NUM_QUBITS, SCREEN_HEIGHT, GRAY, WHITE, BLACK, WIN_SCORE
from utils.resources import Font

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

    if score1 >= WIN_SCORE:
        screen.fill(BLACK)

        gameover_text = "Game Over"
        text = font.gameover_font.render(gameover_text, 1, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 10))
        screen.blit(text, text_pos)

        gameover_text = "Classical computer"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 22))
        screen.blit(text, text_pos)

        gameover_text = "still rules the world"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 27))
        screen.blit(text, text_pos)

    elif score2 >= WIN_SCORE:
        
        screen.fill(BLACK)

        gameover_text = "Congratulations!"
        text = font.gameover_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 10))
        screen.blit(text, text_pos)

        gameover_text = "You demonstrated quantum supremacy"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 22))
        screen.blit(text, text_pos)

        gameover_text = "for the first time in human history!"
        text = font.replay_font.render(gameover_text, 5, WHITE)
        text_pos = text.get_rect(center=(WINDOW_WIDTH / 2, WIDTH_UNIT * 27))
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


def comp_basis_states(num_qubits):
    basis_states = []
    for idx in range(2**num_qubits):
        state = format(idx, '0' + str(num_qubits) + 'b')
        basis_states.append(state)
    return basis_states