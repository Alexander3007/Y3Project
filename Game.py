import random

import pandas as pd
import pygame

from Card import Card


class Game():
    def __init__(self, X, Y, menu):

        self.menu = menu
        self.card_iterator = 0

        # Set initial values for factors
        self.factor_money = 50
        self.factor_happiness = 50
        self.factor_opposition = 50
        self.factor_army = 50

        # create the display surface object
        # of specific dimension..e(X, Y).
        self.display_surface = pygame.display.set_mode((X, Y))

        # set the pygame window name
        pygame.display.set_caption('The Game')

        # Set the cards up!
        self.all_cards = []

        # Import card data from excel file
        card_data = pd.read_excel(r'card_data.xlsx', engine='openpyxl')

        data = pd.DataFrame(card_data, columns=['ID', 'money', 'happiness', 'opposition', 'army', 'fake'])

        for i, j in data.iterrows():
            self.all_cards.append(Card(X, Y, j[0], j[1], j[2], j[3], j[4]))

        self.card_number = len(self.all_cards)

        # randomize order of cards
        random.shuffle(self.all_cards)

    def game_loop(self, X, Y):

        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)

        # Fonts!
        button_font = pygame.font.SysFont('Corbel', 32)

        color_dark = (100, 100, 100)
        color_light = (170, 170, 170)

        card = self.all_cards[self.card_iterator]
        mouse = pygame.mouse.get_pos()

        # completely fill the surface object
        # with white color
        self.display_surface.fill(white)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        self.display_surface.blit(card.image, card.rect)

        # Display the factors
        money_text = button_font.render("Money: " + str(self.factor_money), True, color_dark)
        self.display_surface.blit(money_text, (75, 25))

        happiness_text = button_font.render("Happiness: " + str(self.factor_happiness), True, color_dark)
        self.display_surface.blit(happiness_text, (75 + (X / 4), 25))

        opposition_text = button_font.render("Opposition: " + str(self.factor_opposition), True, color_dark)
        self.display_surface.blit(opposition_text, (75 + 2 * (X / 4), 25))

        army_text = button_font.render("Army: " + str(self.factor_army), True, color_dark)
        self.display_surface.blit(army_text, (75 + 3 * (X / 4), 25))

        # Button Displayable
        # Support button
        pygame.draw.rect(self.display_surface, color_dark, [(X / 2) + (X / 4) - 200, Y - 50, 175, 40])

        text = button_font.render('SUPPORT', True, color_light)
        self.display_surface.blit(text, ((X / 2) + (X / 4) - 175 - 1, Y - 50 + 5))

        # Denounce Button
        pygame.draw.rect(self.display_surface, color_dark, [(X / 2) - (X / 4), Y - 50, 175, 40])

        text = button_font.render('DENOUNCE', True, color_light)
        self.display_surface.blit(text, ((X / 2) - (X / 4) + 10, Y - 50 + 5))

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Denounce Action
                if (X / 2) - (X / 4) <= mouse[0] <= (X / 2) - (X / 4) + 175 and Y - 50 <= mouse[1] <= Y - 50 + 40:
                    self.factor_money, self.factor_happiness, self.factor_opposition, self.factor_army = card.denounce_action(
                        self.factor_money,
                        self.factor_happiness,
                        self.factor_opposition,
                        self.factor_army)
                    self.card_iterator += 1

                # Support Action
                if (X / 2) + (X / 4) - 200 <= mouse[0] <= (X / 2) + (X / 4) - 200 + 175 and Y - 50 <= mouse[
                    1] <= Y - 50 + 40:
                    self.factor_money, self.factor_happiness, self.factor_opposition, self.factor_army = card.support_action(
                        self.factor_money,
                        self.factor_happiness,
                        self.factor_opposition,
                        self.factor_army)
                    self.card_iterator += 1

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()

            # Draws the surface object to the screen.

            card.update()

            pygame.display.update()

            # Here we will check gameover conditions

            if self.factor_money < 0:
                self.menu.mainloop(self.display_surface)

            if self.factor_money > 100:
                self.menu.mainloop(self.display_surface)

            if self.factor_army < 0:
                self.menu.mainloop(self.display_surface)

            if self.factor_army > 100:
                self.menu.mainloop(self.display_surface)

            if self.factor_opposition < 0:
                self.menu.mainloop(self.display_surface)

            if self.factor_opposition > 100:
                self.menu.mainloop(self.display_surface)

            if self.factor_happiness < 0:
                self.menu.mainloop(self.display_surface)

            if self.factor_happiness > 100:
                self.menu.mainloop(self.display_surface)

            # Check if card maximum has been reached
            if self.card_iterator > self.card_number - 2:
                # here we can do end-of-game things!
                # i.e. election time!
                self.menu.mainloop(self.display_surface)