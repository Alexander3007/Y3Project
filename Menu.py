import urllib.request

import pygame
import pygame_menu

from Game import Game


def start_the_game():
    """
    Method to start a new game from the main menu and run the main game loop.
    """
    game_instance = Game(X, Y, menu)
    # game loop
    while True:
        game_instance.game_loop(X, Y)


def learn_more():
    """
    Method that will bring the user to a page where they can learn more about fake news.
    """
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
    menu.add.button('Learn more!', learn_more)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)
