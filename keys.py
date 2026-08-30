from pygame import Rect
from effects import draw_key_effect


def draw_keys(screen, key_rects, pressed_keys):
    """Малює клавіші, враховуючи які зараз натиснуті"""
    for i, rect in enumerate(key_rects):
        is_pressed = i in pressed_keys
        draw_key_effect(screen, rect, is_pressed)


def create_key_rects(num_keys, start_x=50, start_y=100, key_width=100, key_height=250):
    rects = []
    for i in range(num_keys):
        x = start_x + i * key_width
        rects.append(Rect(x, start_y, key_width, key_height))
    return rects
