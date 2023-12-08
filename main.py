import game                                                                                       
import menu_diff
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import rank

# Start resources
menuwindow = Window(800, 600)
menuwindow.set_title("Space Invaders")
mouse = menuwindow.get_mouse()
                                                                                                                                                     

# Start  menu

play = Sprite("./sprites./play_0.png")
diff = Sprite("./sprites./options_0.png")
ranking = Sprite("./sprites./rankings_0.png")
sair = Sprite("./sprites./quit_0.png")                #C6BC00
fundo = GameImage("./sprites./bg_menu.png")            

sair.x = menuwindow.width/2 - sair.width/2
sair.y = menuwindow.height - sair.height - 25

ranking.x = menuwindow.width/2 - ranking.width/2
ranking.y = sair.y - ranking.height - 25

dificuldade = 1

diff.x = menuwindow.width/2 - diff.width/2
diff.y = ranking.y - diff.height - 25
verifica = True
verifica = True
dificuldade = 1
play.x = menuwindow.width/2 - play.width/2
play.y = diff.y - play.height - 25
immortal_start_time = time.time()
# Loop
while True:
    timePass = time.time() - immortal_start_time
    if timePass >= 0.5:
        if mouse.is_over_area([diff.x, diff.y], [diff.x + diff.width, diff.y + diff.height]) and mouse.is_button_pressed(1):
            dificuldade = menu_diff.setdificuldade()
            immortal_start_time = time.time()

        elif mouse.is_over_area([play.x, play.y], [play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
            if verifica:
                game.startgame(dificuldade)
            immortal_start_time = time.time()

        elif mouse.is_over_area([sair.x, sair.y], [sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
            break

        elif mouse.is_over_area([ranking.x, ranking.y], [ranking.x + ranking.width, ranking.y + ranking.height]) and mouse.is_button_pressed(1):
            rank.show()
            immortal_start_time = time.time()
    fundo.draw()
    play.draw()
    diff.draw()
    ranking.draw()
    sair.draw()
    
    menuwindow.update ()
