import pygame

# Global Variables
white = (255, 255, 255)


class Card(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height, ID, money_change, happiness_change, opposition_change, army_change):
        super().__init__()

        # Set dimensions for the card
        self.surface = pygame.Surface([display_width, display_height])
        self.ID = ID
        self.money_change = money_change
        self.opposition_change = opposition_change
        self.happiness_change = happiness_change
        self.army_change = army_change

        # Load the image
        self.image = pygame.image.load(r'images/Cards/Card' + str(self.ID) + '.png')

        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)

    def support_action(self, factor_money, factor_happiness, factor_opposition, factor_army):
        factor_money += self.money_change
        factor_happiness += self.happiness_change
        factor_opposition += self.opposition_change
        factor_army += self.army_change
        return factor_money, factor_happiness, factor_opposition, factor_army

    def denounce_action(self, factor_money, factor_happiness, factor_opposition, factor_army):
        factor_money -= self.money_change
        factor_happiness -= self.happiness_change
        factor_opposition -= self.opposition_change
        factor_army -= self.army_change
        return factor_money, factor_happiness, factor_opposition, factor_army
