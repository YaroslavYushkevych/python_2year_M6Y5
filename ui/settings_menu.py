import pygame
from buttons import Button
from ui.slider import Slider


class SettingsMenu:
    def __init__(self, screen_rect, initial_volume, initial_keys, min_keys, max_keys, on_change, on_back):
        self.screen_rect = screen_rect
        self.on_change = on_change
        self.on_back = on_back

        cx = screen_rect.centerx
        top = 140

        back_idle = pygame.transform.scale(
            pygame.image.load('assets/images/buttons/exit_unhover.png'), (48, 48)
        )
        back_hover = pygame.transform.scale(
            pygame.image.load('assets/images/buttons/exit_hover.png'), (48, 48)
        )

        self.back_btn = Button(
            40, 30, 48, 48,
            "",
            self._back,
            img_idle=back_idle,
            img_hover=back_hover
        )

        def volume_to_text(v):
            return f"{int(v * 100)}%"

        self.volume_slider = Slider(
            cx - 200, top, 400,
            0.0, 1.0, step=0.01, initial=initial_volume,
            label="Гучність",
            value_to_text = volume_to_text
        )
        self.volume_slider.set_on_change(self._on_volume)

        def keys_to_text(v):
            return str(int(v))

        self.keys_slider = Slider(
            cx - 200, top + 120, 400,
            min_keys, max_keys, step=1, initial=initial_keys,
            label="Кількість клавіш",
        value_to_text = keys_to_text
        )
        self.keys_slider.set_on_change(self._on_keys)

    def _on_volume(self, v):
        if self.on_change:
            self.on_change(float(v), int(self.keys_slider.value))

    def _on_keys(self, v):
        if self.on_change:
            self.on_change(float(self.volume_slider.value), int(v))

    def _back(self):
        if self.on_back:
            self.on_back()

    def draw(self, screen, font):
        title = font.render("Налаштування", True, (0, 0, 0))
        screen.blit(title, title.get_rect(center=(self.screen_rect.centerx, 80)))

        self.back_btn.draw(screen, font)
        self.volume_slider.draw(screen, font)
        self.keys_slider.draw(screen, font)

    def handle_event(self, event):
        self.back_btn.handle_event(event)
        self.volume_slider.handle_event(event)
        self.keys_slider.handle_event(event)
