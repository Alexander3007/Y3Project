import pygame

# Global Variables
white = (255, 255, 255)


class Card(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height, ID):
        super().__init__()

        # Set dimensions for the card
        self.surface = pygame.Surface([display_width, display_height])
        self.ID = ID

        # Load the image
        self.image = pygame.image.load(r'images/Cards/Card' + str(self.ID) + '.png')

        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)

    def support_action(self):
        print("Hello")

    def denounce_action(self):
        print("hello there")
