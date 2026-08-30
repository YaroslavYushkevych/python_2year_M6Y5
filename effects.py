from typing import Optional
from pygame import draw, transform, image
from settings import BLACK

# --- Картинки нот (лише існуючі) ---
C_IMG = transform.scale(image.load('assets/images/notes/c.png'), (50, 50))
D_IMG = transform.scale(image.load('assets/images/notes/d.png'), (50, 50))
E_IMG = transform.scale(image.load('assets/images/notes/e.png'), (50, 50))

NOTE_IMAGES = {
    'C': C_IMG,
    'D': D_IMG,
    'E': E_IMG
}


def draw_key_effect(screen, rect, is_pressed=False, note=None):
    if not is_pressed:
        base_color = (220, 220, 220)
    else:
        base_color = (170, 220, 255)

    draw.rect(screen, base_color, rect, border_radius=8)
    draw.rect(screen, BLACK, rect, 2, border_radius=8)
