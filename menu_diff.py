
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *


def setdificuldade():

    # Start resources
    dificuldadewindow = Window(800, 600)

    mouse = dificuldadewindow.get_mouse()
    clock = pygame.time.Clock()

    fundo = GameImage("./sprites./bg_menu.png")
    facil = Sprite("./sprites./easy_0.png")
    medio = Sprite("./sprites./normal_0.png")
    dificil = Sprite("./sprites./hard_0.png")

    dificil.x = dificuldadewindow.width / 2 - dificil.width / 2
    dificil.y = dificuldadewindow.height - dificil.height - 50

    medio.x = dificuldadewindow.width/2 - medio.width/2
    medio.y = dificil.y - medio.height - 25

    facil.x = dificuldadewindow.width/2 - facil.width/2
    facil.y = medio.y - facil.height - 25
    immortal_start_time = time.time()
    
    # Loop
    while True:
        timePass = time.time() - immortal_start_time
        print(timePass)
        if timePass>= 0.5:
            if mouse.is_over_area([facil.x, facil.y], [facil.x + facil.width, facil.y + facil.height]) and mouse.is_button_pressed(1):
                return 1
            if mouse.is_over_area([medio.x, medio.y], [medio.x + medio.width, medio.y + medio.height]) and mouse.is_button_pressed(1):
                return 1.5
            if mouse.is_over_area([dificil.x, dificil.y], [dificil.x + dificil.width, dificil.y + dificil.height]) and mouse.is_button_pressed(1):
                return 2

        fundo.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
        dificuldadewindow.update()
