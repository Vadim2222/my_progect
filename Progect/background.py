import pygame


class Background():

    def __init__(self, screen):
        """Инициализирует фон."""
        self.screen = screen
        self.image = pygame.image.load('images/fon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль втекущей позиции."""
        self.screen.blit(self.image, self.rect)
