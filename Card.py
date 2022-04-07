import pygame

# Global Variables


width = 200
height = 250

white = (255,255,255)


class Card(pygame.sprite.Sprite):
    def __init__(self, width, height, ID ):
        super().__init__()
        self.width = width
        self.height = height

        # Set dimensions for the card
        self.surface = pygame.Surface([width, height])
        self.ID = ID

        # Load the image
        self.image = pygame.image.load(r'images/Card' + str(self.ID) + '.png')

        self.rect = self.image.get_rect()
        self.rect.center = (600,400)
    def display_image(self):
        self.surface.fill(white)
        self.surface.blit(self.image,(0,0))
