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
