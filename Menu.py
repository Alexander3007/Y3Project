import urllib.request

import pygame
import pygame_menu

from Game import Game


class Menu:
    def __init__(self):
        pygame.init()
        # assigning values to X and Y variable
        self.X = 1200
        self.Y = 700
        self.surface = pygame.display.set_mode((self.X, self.Y))

        color_dark = (100, 100, 100)
        color_light = (170, 170, 170)

        # Handles the sounds

        # engine = sound.Sound()
        # engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, '/home/me/click.ogg')
        # engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, '/home/me/open.ogg')

        self.menu = pygame_menu.Menu('Tweeter', self.X, self.Y,
                                theme=pygame_menu.themes.THEME_BLUE)

        self.menu.add.text_input('Name:', default='John Doe')

        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.button('Learn more!', self.learn_more)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        self.menu.mainloop(self.surface)


    def start_the_game(self):
        """
        Method to start a new game from the main menu and run the main game loop.
        """
        game_instance = Game(self.X, self.Y, self.menu)
        # game loop
        while True:
            game_instance.game_loop(self.X, self.Y)


    def learn_more(self):
        """
        Method that will bring the user to a page where they can learn more about fake news.
        """
        request_url = urllib.request.urlopen(
            'https://docs.google.com/document/d/1BzQ7PH07unRiIMSIndmfJ2Iu9IIXOHgIvytI7JvgxHw/edit#heading=h.hwpaayxhxfw')
        print(request_url.read())


