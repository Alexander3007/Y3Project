import random
import pandas as pd
import pygame
from Card import Card
import time


class Game:
    def __init__(self, screen_width, screen_height, menu, high_score):
        """
        Initialization method called whenever a new game is started from the main menu-
        :param screen_width: Game Screen Width
        :param screen_height: Game Screen Height
        :param menu: Pygame Menu object
        """
        self.high_score = high_score
        self.menu = menu
        self.card_iterator = 0
        self.session_score = 1
        #self.high_score = high_score
        white = (255, 255, 255)

        # Set initial values for factors
        self.factor_money = 50
        self.factor_happiness = 50
        self.factor_opposition = 50
        self.factor_army = 50

        # create the display surface object
        # of specific dimension..e(screen_width, screen_height).
        self.display_surface = pygame.display.set_mode((screen_width, screen_height))

        # set the pygame window name
        pygame.display.set_caption('The Game')

        white = (255,255,255)
        black = (0,0,0)
        self.tips_screen(screen_width, screen_height, white, black)

        # Set the cards up!
        self.all_cards = []

        # Import card data from excel file
        card_data = pd.read_excel(r'card_data.xlsx', engine='openpyxl')

        data = pd.DataFrame(card_data, columns=['ID', 'money', 'happiness', 'opposition', 'army', 'fake', 'is_checked'])

        for i, j in data.iterrows():
            self.all_cards.append(Card(screen_width, screen_height, j[0], j[1], j[2], j[3], j[4], j[5], j[6]))

        self.card_number = 30

        # randomize order of cards
        random.shuffle(self.all_cards)

    def game_loop(self, screen_width, screen_height):
        """
        Main Game Loop.
        :param screen_width: Game Screen Width
        :param screen_height: Game Screen Height
        """
        card = self.all_cards[self.card_iterator]
        mouse = pygame.mouse.get_pos()

        self.draw_game_objects(card, screen_width, screen_height)

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Denounce Action
                if (screen_width / 2) - (screen_width / 4) <= mouse[0] <= (screen_width / 2) - (
                        screen_width / 4) + 175 and screen_height - 50 <= mouse[1] <= screen_height - 50 + 40:
                    self.factor_money, self.factor_happiness, self.factor_opposition, self.factor_army = \
                        card.denounce_action(
                            self.factor_money,
                            self.factor_happiness,
                            self.factor_opposition,
                            self.factor_army)
                    self.card_iterator += 1
                    self.session_score += 1
                    self.notification()

                # Support Action
                if (screen_width / 2) + (screen_width / 4) - 200 <= mouse[0] <= (screen_width / 2) + (
                        screen_width / 4) - 200 + 175 and \
                        screen_height - 50 <= mouse[1] <= screen_height - 50 + 40:
                    self.factor_money, self.factor_happiness, self.factor_opposition, self.factor_army = \
                        card.support_action(
                            self.factor_money,
                            self.factor_happiness,
                            self.factor_opposition,
                            self.factor_army)
                    self.card_iterator += 1
                    self.session_score += 1
                    self.notification()

                # Fake news detector
                if 25 <= mouse[0] <= 225 and \
                        (screen_height / 2) - 50 <= mouse[1] <= (screen_height / 2) + 50 and card.is_checked == "no":
                    if card.is_fake == "yes":
                        self.factor_happiness += 5
                        self.factor_opposition -= 5

                    else:
                        self.factor_happiness -= 5
                        self.factor_opposition += 5

                    card.is_checked = "yes"

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.menu.mainloop(self.display_surface)

            # Draws the surface object to the screen.

            card.update()
            pygame.display.update()

            self.check_game_over(screen_width, screen_height)

    def draw_game_objects(self, card, screen_width, screen_height):
        """
        Method to draw game objects on screen.
        :param card: Current card that is being displayed
        :param screen_width: Game Screen Width
        :param screen_height: Game Screen Height
        """
        white = (255, 255, 255)

        # Fonts!
        button_font = pygame.font.SysFont('Corbel', 32)
        small_font = pygame.font.SysFont('Corbel', 20)
        extra_small_font = pygame.font.SysFont('Corbel', 14)

        color_dark = (100, 100, 100)
        color_light = (170, 170, 170)
        color_red = (255, 25, 25)
        color_green = (25, 255, 25)
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
        self.display_surface.blit(happiness_text, (75 + (screen_width / 4), 25))

        opposition_text = button_font.render("Opposition: " + str(self.factor_opposition), True, color_dark)
        self.display_surface.blit(opposition_text, (75 + 2 * (screen_width / 4), 25))

        army_text = button_font.render("Army: " + str(self.factor_army), True, color_dark)
        self.display_surface.blit(army_text, (75 + 3 * (screen_width / 4), 25))

        # Button Displayable
        # Support button
        pygame.draw.rect(self.display_surface, color_dark,
                         [(screen_width / 2) + (screen_width / 4) - 200, screen_height - 50, 175, 40])

        text = button_font.render('SUPPORT', True, color_light)
        self.display_surface.blit(text, ((screen_width / 2) + (screen_width / 4) - 175 - 1, screen_height - 50 + 5))

        # Denounce Button
        pygame.draw.rect(self.display_surface, color_dark,
                         [(screen_width / 2) - (screen_width / 4), screen_height - 50, 175, 40])

        text = button_font.render('DENOUNCE', True, color_light)
        self.display_surface.blit(text, ((screen_width / 2) - (screen_width / 4) + 10, screen_height - 50 + 5))

        # Round Timer
        round_count = small_font.render("Elections in " + str(self.card_number - self.card_iterator - 1), True,
                                        color_dark)
        self.display_surface.blit(round_count, (75 + 4 * (screen_width / 5), screen_height / 2))

        pygame.draw.rect(self.display_surface, color_light,
                         [25, screen_height / 2 - 10, 175, 40])

        text = small_font.render('THIS IS FAKE NEWS!', True, color_red)
        self.display_surface.blit(text, ((25), screen_height / 2))

        if card.is_checked == "yes":
            if card.is_fake == "no":
                text = extra_small_font.render("Sorry, this wasn't fake news!", True, color_red)
                self.display_surface.blit(text, ((35), screen_height / 2 + 50))
            else:
                text = extra_small_font.render("Good guess! This is fake news.", True, color_green)
                self.display_surface.blit(text, ((35), screen_height / 2 + 50))

    def check_game_over(self, screen_width, screen_height):
        """
        Method to check for different game over conditions.
        """
        # Here we will check game over conditions

        if self.factor_money < 0:
            self.activate_game_over("You have wasted away the entire country's funds and are forced to declare "
                                    "bankruptcy. You are removed by a vote of no confidence.",
                                    screen_width,
                                    screen_height)

        if self.factor_money > 100:
            self.activate_game_over("Your immense wealth has led to accusations of corruption, you are removed from "
                                    "office by your own party.",
                                    screen_width,
                                    screen_height)

        if self.factor_army < 0:
            self.activate_game_over("The army became too weak and you were assassinated by foreign powers...",
                                    screen_width,
                                    screen_height)

        if self.factor_army > 100:
            self.activate_game_over("The army became too strong and a coup d'etat occurred, removing you from power.",
                                    screen_width,
                                    screen_height)

        if self.factor_opposition < 0:
            self.activate_game_over("Declared dictator-for-life, it does not take long until you are poisoned by an "
                                    "ambitious follower...",
                                    screen_width,
                                    screen_height)

        if self.factor_opposition > 100:
            self.activate_game_over("The opposition became too strong and called a vote of no confidence, removing "
                                    "you from power",
                                    screen_width,
                                    screen_height)

        if self.factor_happiness < 0:
            self.activate_game_over("Your people hate you and have risen up in a general revolution, quickly removing "
                                    "you from your position... and your head!",
                                    screen_width,
                                    screen_height)

        if self.factor_happiness > 100:
            self.activate_game_over("The people are overjoyed! Unfortunately, this means that no one actually gets "
                                    "anything done anymore. Your country fails due to a lack in productivity.",
                                    screen_width,
                                    screen_height)

        # Check if card maximum has been reached
        if self.card_iterator == self.card_number - 1:
            self.election_time(screen_width, screen_height)

    def activate_game_over(self, text, screen_width, screen_height):
        """
        Method to end the game and display the game over screen to the player, alongside displaying
        the reason why they lost.
        :param text: Game Over explanation text
        :param screen_width: Game screen width
        :param screen_height: Game screen height
        """

        if self.session_score > self.high_score:
            self.high_score = self.session_score

        red = (255, 0, 0)
        white = (255, 255, 255)
        self.fadeout(screen_width, screen_height, red)
        self.display_surface.fill(red)
        pygame.display.update()
        big_font = pygame.font.SysFont('Corbel', 40)
        font = pygame.font.SysFont('Corbel', 18)

        # create a text surface object,
        # on which text is drawn on it.

        game_over_text = big_font.render("GAME OVER", True, white)
        text = font.render(text, True, white)
        session_score_text = big_font.render("Session Score: " + str(self.session_score), True, white)
        high_score_text = big_font.render("High Score: " + str(self.high_score), True, white)

        # create a rectangular object for the
        # text surface object
        go_rect = game_over_text.get_rect()
        text_rect = text.get_rect()
        session_rect = session_score_text.get_rect()
        high_score_rect = high_score_text.get_rect()

        # set the center of the rectangular object.
        go_rect.center = (screen_width // 2, (screen_height // 2) - 100)
        text_rect.center = (screen_width // 2, screen_height // 2)
        session_rect.center = (screen_width // 2, (screen_height // 2) + 100)
        high_score_rect.center = (screen_width // 2, (screen_height // 2) + 200)

        self.display_surface.blit(game_over_text, go_rect)
        self.display_surface.blit(text, text_rect)
        self.display_surface.blit(session_score_text, session_rect)
        self.display_surface.blit(high_score_text, high_score_rect)

        pygame.display.update()

        time.sleep(4)

        pygame.display.update()

        black = (0, 0, 0)
        white = (255, 255, 255)

        self.tips_screen(screen_width, screen_height, red, white)

        time.sleep(4)
        self.menu.mainloop(self.display_surface)

    def election_time(self, screen_width, screen_height):
        """
        Method for handling what happens if a player completes the game without losing.
        :param screen_width: Game screen width
        :param screen_height: Game screen height
        """
        if self.session_score > self.high_score:
            self.high_score = self.session_score

        blue = (0, 0, 128)
        white = (255, 255, 255)
        # here we can do end-of-game things!
        # i.e. election time!
        self.fadeout(screen_width, screen_height, blue)
        self.display_surface.fill(blue)

        big_font = pygame.font.SysFont('Corbel', 40)
        font = pygame.font.SysFont('Corbel', 18)

        if self.factor_opposition < 50:

            # create a text surface object,
            # on which text is drawn on it.

            election_text = big_font.render("Election Time!", True, white)
            text = font.render("You have successfully completed a term in office, "
                               "and are popular enough to be voted back in!", True, white)

            # create a rectangular object for the
            # text surface object
            election_rect = election_text.get_rect()
            text_rect = text.get_rect()

            # set the center of the rectangular object.
            election_rect.center = (screen_width // 2, (screen_height // 2) - 100)
            text_rect.center = (screen_width // 2, screen_height // 2)

            self.display_surface.blit(election_text, election_rect)
            self.display_surface.blit(text, text_rect)

            session_score_text = big_font.render("Session Score: " + str(self.session_score), True, white)
            high_score_text = big_font.render("High Score: " + str(self.high_score), True, white)

            # create a rectangular object for the
            session_rect = session_score_text.get_rect()
            high_score_rect = high_score_text.get_rect()

            session_rect.center = (screen_width // 2, (screen_height // 2) + 100)
            high_score_rect.center = (screen_width // 2, (screen_height // 2) + 200)

            self.display_surface.blit(session_score_text, session_rect)
            self.display_surface.blit(high_score_text, high_score_rect)

            pygame.display.update()
            time.sleep(4)

            # Start a new game
            game_instance = Game(screen_width, screen_height, self.menu, self.high_score)
            # game loop
            while True:
                game_instance.game_loop(screen_width, screen_height)
        else:
            # create a text surface object,
            # on which text is drawn on it.

            election_text = big_font.render("GAME OVER", True, white)
            text = font.render("You have successfully completed a term in office! "
                               "Unfortunately, you lost the re-elections...", True, white)

            # create a rectangular object for the
            # text surface object
            election_rect = election_text.get_rect()
            text_rect = text.get_rect()

            # set the center of the rectangular object.
            election_rect.center = (screen_width // 2, (screen_height // 2) - 100)
            text_rect.center = (screen_width // 2, screen_height // 2)

            self.display_surface.blit(election_text, election_rect)
            self.display_surface.blit(text, text_rect)

            session_score_text = big_font.render("Session Score: " + str(self.session_score), True, white)
            high_score_text = big_font.render("High Score: " + str(self.high_score), True, white)

            # create a rectangular object for the
            session_rect = session_score_text.get_rect()
            high_score_rect = high_score_text.get_rect()

            session_rect.center = (screen_width // 2, (screen_height // 2) + 100)
            high_score_rect.center = (screen_width // 2, (screen_height // 2) + 200)

            self.display_surface.blit(session_score_text, session_rect)
            self.display_surface.blit(high_score_text, high_score_rect)

            pygame.display.update()
            time.sleep(4)
            self.menu.mainloop(self.display_surface)

    # Utility Functions

    def fadeout(self, screen_width, screen_height, colour):
        """
        Utility function that allows the game to fade out to a certain screen colour.
        :param screen_width: Game screen width
        :param screen_height: Game screen height
        :param colour: Colour to fade out to
        """
        fadeout = pygame.Surface((screen_width, screen_height))
        fadeout = fadeout.convert()
        fadeout.fill(colour)
        for i in range(255):
            fadeout.set_alpha(i)
            self.display_surface.blit(fadeout, (0, 0))
            pygame.display.update()
            time.sleep(0.005)

    def tips_screen(self, screen_width, screen_height, colour, text_colour):
        """
        Similar to the general fadeout method, but used specifically for displaying tips.
        :param screen_width: Game screen width
        :param screen_height: Game screen height
        :param colour: Colour to fade out to
        """

        tips = [
            "Check... Is there a URL given in the source? Does it seem reliable?",
            "Look for spelling and grammatical errors!",
            "Profile photos for fake news accounts are often parodied.",
            "How many likes does the tweet have?",
            "What's the username handle of the person tweeting? Does it seem legitimate?",
            "Look out for verified badges!",
            "Check the amount of background information given by the source!"

        ]
        fadeout = pygame.Surface((screen_width, screen_height))
        fadeout = fadeout.convert()
        fadeout.fill(colour)
        black = (0, 0, 0)
        white = (255, 255, 255)
        chosen_tip = random.randint(0, len(tips)-1)
        for i in range(255):
            fadeout.set_alpha(i)
            self.display_surface.blit(fadeout, (0, 0))
            font = pygame.font.SysFont('Corbel', 24)
            small_font = pygame.font.SysFont('Corbel', 18)

            text = font.render("Loading...", True, text_colour)
            # create a rectangular object for the
            # text surface object
            text_rect = text.get_rect()
            text_rect.center = (screen_width // 2, screen_height // 2)

            fadeout.blit(text, text_rect)


            text = small_font.render("Fake news recognition tip: " + str(tips[chosen_tip]), True, text_colour)

            # create a rectangular object for the
            # text surface object
            text_rect = text.get_rect()
            text_rect.center = (screen_width // 2, (screen_height // 2)+50)

            fadeout.blit(text, text_rect)


            pygame.display.update()
            time.sleep(0.005)

    def loading_screen_fadeout(self, screen_width, screen_height, colour):
        """
        Similar to the general fadeout method, but used specifically for loading screens.
        :param screen_width: Game screen width
        :param screen_height: Game screen height
        :param colour: Colour to fade out to
        """
        fadeout = pygame.Surface((screen_width, screen_height))
        fadeout = fadeout.convert()
        fadeout.fill(colour)
        black = (0, 0, 0)
        for i in range(255):
            fadeout.set_alpha(i)
            self.display_surface.blit(fadeout, (0, 0))

            font = pygame.font.SysFont('Corbel', 24)
            text = font.render("Loading...", True, black)

            # create a rectangular object for the
            # text surface object
            text_rect = text.get_rect()
            text_rect.center = (screen_width // 2, screen_height // 2)

            fadeout.blit(text, text_rect)

            pygame.display.update()
            time.sleep(0.005)

    def get_session_score(self):
        return self.session_score

    def notification(self):
        notification_sound = pygame.mixer.Sound("twitter_alert.mp3")
        pygame.mixer.Sound.play(notification_sound)
