import pygame
import pygame_menu
from pygame_menu import sound
import urllib.request
from Card import Card

pygame.init()
# assigning values to X and Y variable
X = 1200
Y = 800
surface = pygame.display.set_mode((X, Y))

#Handles the sounds

#engine = sound.Sound()
#engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, '/home/me/click.ogg')
#engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, '/home/me/open.ogg')

def start_the_game():
    # define the RGB value for white,
    #  green, blue colour .
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)


    # Create a for loop to instantiate cards

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Show Text')

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 24)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('The game will appear here...', True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)


    allCards = pygame.sprite.Group()

    card = Card(200, 300, 0)

    allCards.add(card)

    # infinite loop
    while True:

        # completely fill the surface object
        # with white color
        display_surface.fill(white)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display_surface.blit(card.image, card.rect)

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

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
            card.display_image()

            pygame.display.update()
    pass

def learn_more():
    #For Later
    pass




menu = pygame_menu.Menu('Twitter', X, Y,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name:', default='John Doe')


menu.add.button('Play', start_the_game)
menu.add.button('Learn more',learn_more)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)