from pygame import *
from settings import *
from sounds import load_sounds
from keys import draw_keys, create_key_rects
from buttons import Button

init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano Game")

sounds = load_sounds(KEYS)
key_rects = create_key_rects(len(KEYS))
keys_list = list(KEYS.keys())
my_font = font.SysFont("Arial", 24)
pressed_keys = set()

# кнопки меню
def start_game(): pass
def open_settings(): pass
def exit_game(): quit()

buttons = [
    Button(60, 20, 120, 40, "Settings", open_settings)
]

running = True
while running:
    screen.fill(WHITE)

    # кнопки
    for button in buttons:
        button.draw(screen, my_font)

    # клавіші
    draw_keys(screen, key_rects, pressed_keys)

    display.flip()

    for e in event.get():
        if e.type == QUIT:
            running = False

        # кнопки
        for button in buttons:
            button.handle_event(e)

        # клавіатура
        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
                idx = keys_list.index(k)
                pressed_keys.add(idx)

        if e.type == KEYUP:
            k = key.name(e.key)
            if k in sounds:
                idx = keys_list.index(k)
                if idx in pressed_keys:
                    pressed_keys.remove(idx)

        # миша по клавішах
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)

        if e.type == MOUSEBUTTONUP:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if i in pressed_keys and rect.collidepoint(pos):
                    pressed_keys.remove(i)
