import pygame.mixer
from pygame import mixer

pygame.mixer.init()
def load_sounds(keys):
    sounds = {}
    for key, filename in keys.items():
        sounds[key] = mixer.Sound(f"assets/sounds/{filename}")
    return sounds
