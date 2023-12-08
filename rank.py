from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

def show():
    gamewindow = Window(800, 600)
    gamewindow.set_background_color([0, 0, 0])
    gamewindow.set_title("Space Invaders")
    teclado = gamewindow.get_keyboard()
    fundoOp = GameImage("./sprites./bg_menu.png")
    file = open('Ranking.txt','r')
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    
    lines.sort(key=lambda line:int(line.strip().split("=")[1]), reverse=True)
    if (len(lines) > 5):
        lines = lines[:5]
    while True:
        fundoOp.draw()
        gamewindow.draw_text("RANKING :",20,  20 , 45, (50,205,50), "Arial", False, False)
        for i in range(len(lines)):
            gamewindow.draw_text("{}".format(lines[i]),20, (i * 50) + 100 + 20 , 45, (50,205,50), "Arial", False, False)
        if teclado.key_pressed("ESC"):
            return

        
        
        gamewindow.update()