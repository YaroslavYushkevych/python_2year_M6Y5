from pygame import Rect, mouse, transform, image, MOUSEBUTTONDOWN, draw


class Button:
    def __init__(
        self,
        x, y, width, height,
        text: str = "",
        action=None,
        img_idle=None,
        img_hover=None,
        center: bool = False
    ):
        self.text = text
        self.action = action
        self.img_idle = img_idle
        self.img_hover = img_hover
        self.use_image = img_idle is not None

        self.color_idle = (200, 200, 200)
        self.color_hover = (180, 180, 180)
        self.color_border = (0, 0, 0)
        self.text_color = (0, 0, 0)

        if self.use_image and (width is None or height is None):
            iw, ih = self.img_idle.get_size()
            width = width or iw
            height = height or ih

        if center:
            self.rect = Rect(0, 0, width, height)
            self.rect.center = (x, y)
        else:
            self.rect = Rect(x, y, width, height)

    def draw(self, screen, font):
        mouse_pos = mouse.get_pos()
        hovered = self.rect.collidepoint(mouse_pos)

        if self.use_image:
            surf = (self.img_hover if (hovered and self.img_hover) else self.img_idle)
            if surf.get_size() != (self.rect.w, self.rect.h):
                surf = transform.scale(surf, (self.rect.w, self.rect.h))
            screen.blit(surf, self.rect.topleft)

            if self.text:
                text_surf = font.render(self.text, True, self.text_color)
                screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))
        else:
            color = self.color_hover if hovered else self.color_idle
            draw.rect(screen, color, self.rect, border_radius=8)
            draw.rect(screen, self.color_border, self.rect, 2, border_radius=8)

            if self.text:
                text_surf = font.render(self.text, True, self.text_color)
                screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()
