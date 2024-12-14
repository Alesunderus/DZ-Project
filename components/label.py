import pygame

fonts = []

anti_alias = True
font_folder_path = 'static/fonts'


class Label:
    def __init__(self, font, text, size = 32, color = (255,255,255)):
        from core.engine import engine
        global labels
        self.color = color
        if font in fonts:
            self.font = font
        else:
            self.font = pygame.font.Font(font_folder_path + '/' + font, size)

        self.set_text(text)
        engine.ui_drawables.append(self)

    def get_bounds(self):
        return pygame.Rect(0,0,self.surface.get_width(), self.surface.get_height())

    def breakdown(self):
        from core.engine import engine
        engine.ui_drawables.remove(self)

    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, anti_alias, self.color)
        self.shadow_surface = self.font.render(self.text, anti_alias, (0,0,0))

    def draw(self, screen):
        screen.blit(self.shadow_surface, (self.entity.x+1, self.entity.y+1))
        screen.blit(self.surface, (self.entity.x, self.entity.y))