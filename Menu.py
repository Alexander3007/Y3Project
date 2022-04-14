import pygame
import pygame_menu
from pygame_menu import sound
import pandas as pd
import random
import urllib.request
from Card import Card


def start_the_game():
    card_iterator = 0
    # define the RGB value for white,
    #  green, blue colour .
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # Set initial values for factors
    factor_money = 50
    factor_happiness = 50
    factor_opposition = 50
    factor_army = 50

    # Fonts!
    button_font = pygame.font.SysFont('Corbel', 32)

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('The Game')

    # Set the cards up!
    all_cards = []

    # Import card data from excel file
    card_data = pd.read_excel(r'card_data.xlsx', engine='openpyxl')

    data = pd.DataFrame(card_data, columns=['ID', 'money', 'happiness', 'opposition', 'army', 'fake'])

    for i, j in data.iterrows():
        all_cards.append(Card(X, Y, j[0], j[1], j[2], j[3], j[4]))

    card_number = len(all_cards)

    # randomize order of cards
    random.shuffle(all_cards)
    # game loop
    while True:
        card = all_cards[card_iterator]
        mouse = pygame.mouse.get_pos()

        # completely fill the surface object
        # with white color
        display_surface.fill(white)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display_surface.blit(card.image, card.rect)

        # Display the factors
        money_text = button_font.render("Money: " + str(factor_money), True, color_dark)
        display_surface.blit(money_text, (75, 25))

        happiness_text = button_font.render("Happiness: " + str(factor_happiness), True, color_dark)
        display_surface.blit(happiness_text, (75 + (X / 4), 25))

        opposition_text = button_font.render("Opposition: " + str(factor_opposition), True, color_dark)
        display_surface.blit(opposition_text, (75 + 2*(X / 4), 25))

        army_text = button_font.render("Army: " + str(factor_army), True, color_dark)
        display_surface.blit(army_text, (75 + 3*(X / 4), 25))

        # Button Displayable
        # Support button
        pygame.draw.rect(display_surface, color_dark, [(X / 2) + (X / 4) - 200, Y - 50, 175, 40])

        text = button_font.render('SUPPORT', True, color_light)
        display_surface.blit(text, ((X / 2) + (X / 4) - 175 - 1, Y - 50 + 5))

        # Denounce Button
        pygame.draw.rect(display_surface, color_dark, [(X / 2) - (X / 4), Y - 50, 175, 40])

        text = button_font.render('DENOUNCE', True, color_light)
        display_surface.blit(text, ((X / 2) - (X / 4) + 10, Y - 50 + 5))

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Denounce Action
                if (X / 2) - (X / 4) <= mouse[0] <= (X / 2) - (X / 4) + 175 and Y - 50 <= mouse[1] <= Y - 50 + 40:
                    factor_money, factor_happiness, factor_opposition, factor_army = card.denounce_action(factor_money,
                                                                                                          factor_happiness,
                                                                                                          factor_opposition,
                                                                                                          factor_army)
                    card_iterator += 1

                # Support Action
                if (X / 2) + (X / 4) - 200 <= mouse[0] <= (X / 2) + (X / 4) - 200 + 175 and Y - 50 <= mouse[1] <= Y - 50 + 40:
                    factor_money, factor_happiness, factor_opposition, factor_army = card.support_action(factor_money,
                                                                                                         factor_happiness,
                                                                                                         factor_opposition,
                                                                                                         factor_army)
                    card_iterator += 1

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

            if factor_money < 0:
                menu.mainloop(display_surface)

            if factor_money > 100:
                menu.mainloop(display_surface)

            if factor_army < 0:
                menu.mainloop(display_surface)

            if factor_army > 100:
                menu.mainloop(display_surface)

            if factor_opposition < 0:
                menu.mainloop(display_surface)

            if factor_opposition > 100:
                menu.mainloop(display_surface)

            if factor_happiness < 0:
                menu.mainloop(display_surface)

            if factor_happiness > 100:
                menu.mainloop(display_surface)

            # Check if card maximum has been reached
            if card_iterator > card_number - 2:
                # here we can do end-of-game things!
                # i.e. election time!
                menu.mainloop(display_surface)


def learn_more():
    request_url = urllib.request.urlopen(
        'https://docs.google.com/document/d/1BzQ7PH07unRiIMSIndmfJ2Iu9IIXOHgIvytI7JvgxHw/edit#heading=h.hwpaayxhxfw')
    print(request_url.read())


if __name__ == '__main__':
    pygame.init()
    # assigning values to X and Y variable
    X = 1200
    Y = 700
    surface = pygame.display.set_mode((X, Y))

    color_dark = (100, 100, 100)
    color_light = (170, 170, 170)

    # Handles the sounds

    # engine = sound.Sound()
    # engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, '/home/me/click.ogg')
    # engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, '/home/me/open.ogg')

    menu = pygame_menu.Menu('Tweeter', X, Y,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name:', default='John Doe')

    menu.add.button('Play', start_the_game)
    menu.add.button('Learn more', learn_more)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)
