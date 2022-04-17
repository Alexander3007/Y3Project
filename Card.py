import pygame
from Utility import resource_path


class Card(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height, ID, money_change, happiness_change, opposition_change,
                 army_change, is_fake):
        """
        Initialization function for the cards, called when all the cards are created before the game starts.
        :param display_width: Game screen width
        :param display_height: Game screen height
        :param ID: Card unique identifier number
        :param money_change: Card's money level modifier
        :param happiness_change: Card's happiness level modifier
        :param opposition_change: Card's opposition level modifier
        :param army_change: Card's army level modifier
        """
        super().__init__()

        # Set dimensions for the card
        self.surface = pygame.Surface([display_width, display_height])
        self.ID = ID
        self.money_change = money_change
        self.opposition_change = opposition_change
        self.happiness_change = happiness_change
        self.army_change = army_change
        self.is_fake = is_fake

        # Load the image
        #image_asset = resource_path(r'images/Cards/Card' + str(self.ID) + '.png')

        # DISTRIBUTION CODE
        #self.image = pygame.image.load(r'Menu/images/Cards/Card' + str(self.ID) + '.png')

        # PYTHON CODE
        self.image = pygame.image.load(r'images/Cards/Card' + str(self.ID) + '.png')

        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)

    def support_action(self, factor_money, factor_happiness, factor_opposition, factor_army):
        """
        Method called whenever a player selects the support action for a card
        :param factor_money: Value representing money level
        :param factor_happiness: Value representing happiness level
        :param factor_opposition: Value representing opposition level
        :param factor_army: Value representing army level
        :return: updated values for all factors
        """
        factor_money += self.money_change
        factor_happiness += self.happiness_change
        factor_opposition += self.opposition_change
        factor_army += self.army_change
        return factor_money, factor_happiness, factor_opposition, factor_army

    def denounce_action(self, factor_money, factor_happiness, factor_opposition, factor_army):
        """
        Method called whenever a player selects the denounce action for a card
        :param factor_money: Value representing money level
        :param factor_happiness: Value representing happiness level
        :param factor_opposition: Value representing opposition level
        :param factor_army: Value representing army level
        :return: updated values for all factors
        """

        factor_money -= self.money_change
        factor_happiness -= self.happiness_change
        factor_opposition -= self.opposition_change
        factor_army -= self.army_change
        return factor_money, factor_happiness, factor_opposition, factor_army
