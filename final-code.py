"""
Final Project: Interactive Storyboard

Authors: Nguyen Phuong Anh, Bui Dinh Khoi, Pham Hoang Nhat Phuong, Pho Do Quyen, Trinh The Vinh

The program uses pygame to display the story "Turtle and Rabbit" as a game with images & sounds, providing the users with options to choose and decide the story

The font credit belongs to github.com/baraltech/
"""

#import libraries
import time
import pygame, sys
from button import Button
from pygame import mixer

#intialize pygame & mixer libraries
pygame.init()
mixer.init()

#set the screen size and caption
SCREEN = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("The Turtle and The Rabbit")

#constance
SCREEN_POS = (0, 0)
BUTTON_1_POS = (500, 600)
BUTTON_2_POS = (500, 650)
PAUSE = 1
#add background sound
INFINITE = -1
mixer.music.load("forest.mp3")
mixer.music.play(INFINITE)

def welcome():
    """This function prints the welcome instruction of the story"""
    BG = pygame.image.load("1.gif")
    BUTTON_POS = (500, 550)
    #X, Y are button coordinates
    X1 = 497
    Y1 = 247
    X2 = 500
    Y2 = 250
    SCALE = 70
    
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        text = "Welcome to the game! \nThis story is based on the story called \n 'the Turtle and the Rabbit'"
        lines = text.splitlines()
        
        for i, l in enumerate(lines):
            BOLD_TEXT = get_font(20).render(l, True, "black")
            MENU_TEXT = get_font(20).render(l, True, "white")
            BOLD_RECT = BOLD_TEXT.get_rect(center=(X1, Y1 + i*SCALE))
            MENU_RECT = MENU_TEXT.get_rect(center=(X2, Y2 + i*SCALE))
            SCREEN.blit(BOLD_TEXT, BOLD_RECT)
            SCREEN.blit(MENU_TEXT, MENU_RECT)
            
        A = Button(insert_image=None, position=BUTTON_POS, 
                            display_text="CONTINUE", text_font=get_font(20), preset_color="#d7fcd4", mouse_over_color="White")
        A.change_color(MOUSE_POS)
        A.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    main_menu()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
        pygame.display.update()

def main_menu():
    """This function prints the story menu"""
    BG = pygame.image.load("1.gif")
    X, Y = 500, 300
    BUTTON_A_POS = (500, 400)
    BUTTON_B_POS = (500, 450)
    
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        text = "Do you want to play the story?"
        BOLD_TEXT = get_font(30).render(text, True, "orange")
        MENU_TEXT = get_font(30).render(text, True, "yellow")
        BOLD_RECT = BOLD_TEXT.get_rect(center=(X-2, Y-2))
        MENU_RECT = MENU_TEXT.get_rect(center=(X, Y))
        
        A = Button(insert_image=None, position=BUTTON_A_POS, 
                            display_text="YES", text_font=get_font(25), preset_color="#d7fcd4", mouse_over_color="White")
        B = Button(insert_image=None, position=BUTTON_B_POS, 
                            display_text="NO", text_font=get_font(25), preset_color="#d7fcd4", mouse_over_color="White")

        SCREEN.blit(BOLD_TEXT, BOLD_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [A, B]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MENU_MOUSE_POS):
                    checkpoint_1()
                if B.check_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def checkpoint_1():#The race begins go to 2 & 5
    """Begin the game story after user press YES. Provide to user two options to go first or not"""
    START = mixer.Sound("start.wav")
    START.play()
    lines, BG = checkpoint_setup('1.gif', 'text_1.txt')
    islast = False
    not_draw_text = True

    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
        
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options('Yes', 'No', MOUSE_POS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_2()
                if B.check_input(MOUSE_POS):
                    checkpoint_5()
        pygame.display.update()
        
def checkpoint_2(): #The rabbit waits go to 3 and 4
    """Turtle go first and two options for rabbit (sleep or explore)"""
    lines, BG = checkpoint_setup('2.gif', 'text_2.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()  
        A, B = draw_options('Take a nap', 'Explore the forest', MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_3()
                if B.check_input(MOUSE_POS):
                    checkpoint_4()
        pygame.display.update()

def checkpoint_3(): #Take a nap go to log
    """Rabbit take a nap and late. Continute the game by move to the log round"""
    SNORING = mixer.Sound("snoring.wav")
    SNORING.play()
    lines, BG = checkpoint_setup('3.gif', 'text_3.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'After a while', '3.5.png')
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A = draw_options('Continue', '', MOUSE_POS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_8()
        pygame.display.update()

def checkpoint_4(): #Explore the forest then log
    """Rabbit explore the forest"""
    FOREST = mixer.Sound("forest2.wav")
    FOREST.play()
    lines, BG = checkpoint_setup('4.gif', 'text_4.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'Then Rabbit realizes', '4.5.gif')
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A = draw_options('Continue', '', MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_log()
        pygame.display.update()
        

def checkpoint_5(): #RABBIT RUNS FIRST then 6 and 7
    """Rabbit go first and get two options"""
    RABBITSTEP = mixer.Sound("rabbitstep.wav")
    RABBITSTEP.play()
    lines, BG = checkpoint_setup('5.gif', 'text_5.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG= draw_text(MOUSE_POS, BG, lines, islast, 'But suddenly', '5.5.gif')
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options('Find another route', 'Ask for help', MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_6()
                if B.check_input(MOUSE_POS):
                    checkpoint_7()
        pygame.display.update()
        
def checkpoint_6(): #TAKE ANOTHER ROUTE => 5
    """find another route"""
    RABBITSTEP = mixer.Sound("rabbitstep.wav")
    lines, BG = checkpoint_setup('6.gif', 'text_6.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'However, when', '6.5.gif')
        RABBITSTEP.play()
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()     
        A = draw_options('Replay from last checkpoint', '', MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_log()
        pygame.display.update()
        
def checkpoint_log(): #6 or 7
    """ Rabbit meets the log"""
    lines, BG = checkpoint_setup('log.gif', 'text_log.txt')
    islast = False
    not_draw_text = True

    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options('Ask for help', 'Find another route', MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_7()
                if B.check_input(MOUSE_POS):
                    checkpoint_6()
        pygame.display.update()
        
def checkpoint_7(): #ask for help then 9 and 10
    """Ask bear to help and get two options"""
    TALKTOBEAR = mixer.Sound("rabbittalkbear.wav")
    TALKTOBEAR.play()
    lines, BG = checkpoint_setup('7.gif', 'text_7.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options('Throw it into the river to block turtle', 'Keep going', MOUSE_POS)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                   checkpoint_9()
                if B.check_input(MOUSE_POS):
                   checkpoint_10()  
        pygame.display.update()

def checkpoint_8(): #broke leg from taking a nap => go to 3
    """Rabbit thow the log and broke leg after take a nap and throw the log"""
    FAIL = mixer.Sound("fail.wav")
    RABBITSIGHS = mixer.Sound("rabbitsighs.wav")
    DROPINRIVER = mixer.Sound("dropintoriver.wav")
    RABBITSIGHS.play()
    FAIL.play()
    lines, BG = checkpoint_setup('8.gif', 'text_8.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'But without', '8.5.gif')
        DROPINRIVER.play()
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A = draw_options('Replay from last checkpoint', '', MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_2()
        pygame.display.update()

def checkpoint_9(): #broke leg from ask for regular help => go to 7
    """Throw the log into the river after ask bear for help. And broke leg"""
    DROPINRIVER = mixer.Sound("dropintoriver.wav")
    lines, BG = checkpoint_setup('9.gif', 'text_9.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'But when Rabbit', '9.5.gif')
        DROPINRIVER.play()
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A = draw_options('Replay from last checkpoint', '', MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_7() 
        pygame.display.update()

def checkpoint_10(): #keep going then 11 and 16
    """Keep going after bear help move the log and get two more option."""
    THANKU = mixer.Sound("thanku.wav")
    THANKU.play()
    lines, BG = checkpoint_setup('10.png', 'text_10.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'Then Rabbit faces', '10.5.gif')
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options('Delicious cake! I must buy one', 'Keep going', MOUSE_POS)

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if A.check_input(MOUSE_POS):
                   checkpoint_11()
               if B.check_input(MOUSE_POS):
                   checkpoint_16()   
        pygame.display.update()

def checkpoint_11(): #buy the cake then 12 and 13
    """Come to the bakery and decide to eat or take away"""
    CAKE = mixer.Sound("rabbiteatcake.wav")
    CAKE.play()
    lines, BG = checkpoint_setup('11.gif', 'text_11.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options('Eat it here at the bakery', 'Take away', MOUSE_POS)

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if A.check_input(MOUSE_POS):
                   checkpoint_12()
               if B.check_input(MOUSE_POS):
                   checkpoint_13() 
        pygame.display.update()

def checkpoint_12(): #eat at the store then lost =>11
    """ After eat at the bakery, get lost and lose the game."""
    FAIL = mixer.Sound("fail.wav")
    FAIL.play()
    lines, BG = checkpoint_setup('12.gif', 'text_12.txt')
    islast = False
    not_draw_text = True
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'Then Bird', '12.5.gif')
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A = draw_options('Replay from last checkpoint', '', MOUSE_POS)

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if A.check_input(MOUSE_POS):
                   checkpoint_11()
        pygame.display.update()
    
def checkpoint_13(): #take away then 14 and 15
    """ Take cake away and meet turtle turned over. Get two options"""
    RABBITSTEP = mixer.Sound("rabbitstep.wav")
    RABBITSTEP.play()
    lines, BG = checkpoint_setup('13.gif', 'text_13.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, 'But wait', '13.5.gif')
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options('Give turtle the cake', 'Sprint towards the finish line', MOUSE_POS)

        for event in pygame.event.get():
           if event.type == pygame.MOUSEBUTTONDOWN:
               if A.check_input(MOUSE_POS):
                   checkpoint_15()
               if B.check_input(MOUSE_POS):
                   checkpoint_14()
        pygame.display.update()
    
def checkpoint_14(): #ignore turtle then 13
    """Sprint toward to finish the game"""
    WIN = mixer.Sound("win.wav")
    WIN.play()
    lines, BG = checkpoint_setup('14.gif', 'text_14.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A = draw_options("Replay from last checkpoint", '', MOUSE_POS)
       
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
               if A.check_input(MOUSE_POS):
                    checkpoint_13()
        pygame.display.update()

def checkpoint_15(): #share cake then end win => 1
    """Help turtle and win the game together"""
    WIN = mixer.Sound("win.wav")
    WIN.play()
    lines, BG = checkpoint_setup('15.gif', 'text_15.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()  
        A = draw_options("You won the race! Play again", '', MOUSE_POS)           

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_1()
        pygame.display.update()
        
def checkpoint_16(): #don't eat cake => 17 and 18
    """Keep going from the bakery"""
    lines, BG = checkpoint_setup('16.png', 'text_16.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options("Help the turtle flip on its back", "Sprint towards the finish line", MOUSE_POS)                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_18()
                if B.check_input(MOUSE_POS):
                    checkpoint_17()
        pygame.display.update()

def checkpoint_17(): #ignore turtle > 1
    """Sprint toward to finish the game"""
    RABBITSTEP = mixer.Sound("rabbitstep.wav")
    GETHELP = mixer.Sound("help.wav")
    WIN = mixer.Sound("win.wav")
    GETHELP.play()
    RABBITSTEP.play()
    WIN.play()
    lines, BG = checkpoint_setup('17.png', 'text_17.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A = draw_options("You won the race. Play again", '', MOUSE_POS)                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_1()
        pygame.display.update()
        
def checkpoint_18(): #help turtle
    """Help turtle and win the game together"""
    GETHELP = mixer.Sound("help.wav")
    WIN = mixer.Sound("win.wav")
    GETHELP.play()
    WIN.play()
    lines, BG = checkpoint_setup('18.png', 'text_18.txt')
    islast = False
    not_draw_text = True
    
    while not_draw_text:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        not_draw_text, BG = draw_text(MOUSE_POS, BG, lines, islast, None, None)
    while True:
        SCREEN.blit(BG, SCREEN_POS)
        MOUSE_POS = pygame.mouse.get_pos()
        A, B = draw_options("Replay from the beginning", "Exit game", MOUSE_POS)   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.check_input(MOUSE_POS):
                    checkpoint_1()
                if B.check_input(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def get_text(textfile):
    """
    This fucntion read the textfile.
    
    Parameter: textfile - a text file contains the text to load (.txt)
    
    
    """
    infile = open(textfile, encoding='utf8')
    return infile.read()

def get_font(size): 
    """"
    This function gets the font and size from the font.ttf file
    
    Parameter: size - an integer represents the character size
    
    Return: the font to be used
    """
    FONT = 'font.ttf'
    return pygame.font.Font(FONT, size)

def checkpoint_setup(scene_image, scene_text):
    """
    This function setups the background images and split the text provided by lines
    
    Parameters:
        scene_image - the background image to be displayed in that checkpoint
        scene_text - the text used in that checkpoint
        
    Returns:
        lines - the list of lines in the text
        BG - background screen
    
    """
    SCREEN_POS = (1000, 500)
    SCREEN.fill("black")
    BG = pygame.image.load(scene_image)
    BG = pygame.transform.scale(BG, SCREEN_POS)
    text = get_text(scene_text)
    lines = text.split('\n')
    return lines, BG

def draw_text(mouse_control, BG, lines, islast, switch_text, switch_to_image):
    """This function draws the text of the checkpoint on the screen

    Parameters:
        mouse_control - the get position of the mouse
        BG - the screen image
        lines - the list of lines in the provided txt
        islast - the variable check whether the line is the last one
        switch_text - the text to indicate the program to switch the scene to the new image
        switch_to_image - the new image that we use to switch
        
    Returns:
        not_draw_text - whether the text is drawn
        BG - the background image
    """
    NEW_SCREEN_POS = (1000, 500)
    if not islast:
        for i, l in enumerate(lines):
            if switch_text != None:
                if switch_text in l:
                    SCREEN.fill("black")
                    BG = pygame.image.load(switch_to_image)
                    BG = pygame.transform.scale(BG, NEW_SCREEN_POS)
                    SCREEN.blit(BG, SCREEN_POS)
            if l == lines[-1]:
                lines = l
                islast = True
                break
            else:
                pygame.display.update()
                A_TEXT = get_font(12).render(l, True, "White")
                A_RECT = A_TEXT.get_rect(center=BUTTON_1_POS)
                SCREEN.blit(A_TEXT, A_RECT)
                pygame.display.update()
                time.sleep(PAUSE)
                pygame.draw.rect(SCREEN, ('black'), A_RECT)
                
    A_TEXT = get_font(13).render(lines, True, "White")
    A_RECT = A_TEXT.get_rect(center=(500, 550))
    SCREEN.blit(A_TEXT, A_RECT)
    pygame.display.update()
    not_draw_text = False
    return not_draw_text, BG

def draw_options(text_1, text_2, mouse_control):
    """This fuction creates two options of the game play"""
    button_1 = Button(insert_image=None, position=BUTTON_1_POS, 
                        display_text=text_1, text_font=get_font(12), preset_color="White", mouse_over_color="Green")
    
    button_1.change_color(mouse_control)
    button_1.update(SCREEN)
    
    if text_2 != '':
        button_2 = Button(insert_image=None, position=BUTTON_2_POS, 
                        display_text= text_2, text_font=get_font(12), preset_color="White", mouse_over_color="Green")
    
        button_2.change_color(mouse_control)
        button_2.update(SCREEN)
        return button_1, button_2
    
    return button_1

welcome()