import pygame
import pygame_menu
from pygame_menu import sound


pygame.init()
surface = pygame.display.set_mode((600, 400))

#Handles the sounds

#engine = sound.Sound()
#engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, '/home/me/click.ogg')
#engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, '/home/me/open.ogg')

def start_the_game():
    #For Later
    pass

def learn_more():
    #For Later
    pass




menu = pygame_menu.Menu('Twitter', 600, 400,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')


menu.add.button('Play', start_the_game)
menu.add.button('Learn more',learn_more)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)