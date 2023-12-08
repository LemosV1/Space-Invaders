from PPlay.window import *
from PPlay.sprite import *
import random
import time

def generate_monsters(L, C, monster):
    matMons = [[Sprite("./sprites/enemy.png") for _ in range(C)] for _ in range(L)]
    for i in range(L):
        for j in range(C):
            matMons[i][j].set_position((j*(monster.width + monster.width / 2)+10), (i * (monster.height + monster.height / 2)+30))
    return matMons

def startgame(dificuldade):

    # Start resources

    gamewindow = Window(800, 600)
    gamewindow.set_background_color([0, 0, 0])
    gamewindow.set_title("Space Invaders")
    monster = Sprite("./sprites/enemy.png")
    teclado = gamewindow.get_keyboard()
    L = 4
    C = 4

    is_immortal = False
    immortal_start_time = None
    Parar_start_time = None
    Parar = False

    contaTiro = 0  # Contador tiro
    tiro_monstro = 0
    
    matMons = [[Sprite("./sprites/enemy.png") for _ in range(C)] for _ in range(L)]
    for i in range(L):
        for j in range(C):
            matMons[i][j].set_position((j*(monster.width + monster.width / 2)+10), (i * (monster.height + monster.height / 2)+30))

    # Player e tiros
    player = Sprite("./sprites/player.png")
    vel_player = 200
    player.set_position(gamewindow.width/2 - player.width/2, (gamewindow.height - player.height) - 10)
    vtiro = []
    vel_tiro = -500
    mtiro = []
    vel_tiro_m = 400
    
    monsVel = 100
    especial = False

    vida = Sprite("./sprites/vida.png")
    vet_vida = [Sprite("./sprites/vida.png") for _ in range(3)]
    for i in range(3):
            vet_vida[i].set_position(150 + i*(vida.width),10)
    
    pontos = 0
    paralisar = 1

    fundo = Sprite("./sprites/bg_menu.png")
    
    clock = pygame.time.Clock()

    # GameLoop
    while True:
        clock.tick()
        fps = clock.get_fps()

        # Contadores
        contaTiro += gamewindow.delta_time()
        tiro_monstro += gamewindow.delta_time()

        if teclado.key_pressed("ESC"):
            break

        # Tiro
        if teclado.key_pressed("SPACE") and contaTiro > (0.5 * dificuldade):
            tiro = Sprite("./sprites/bullet.png")
            tiro.set_position(player.x + player.width/2, player.y - tiro.height)
            vtiro.append(tiro)
            contaTiro = 0
        for i in range(len(vtiro)):
            vtiro[i].move_y((vel_tiro * dificuldade) * gamewindow.delta_time())
            if vtiro[i].y < 0 - vtiro[i].height:
                vtiro.pop(i)
                break
        
        #Recriar monstros
        if not any(matMons):
            dificuldade += 0.1
            matMons = generate_monsters(L, C, monster)

        #Tiro Monstros
        while(tiro_monstro > (2 * dificuldade)):
            if len(matMons) > 0 and all(len(row) > 0 for row in matMons):
                l_rand = random.randint(0, len(matMons) - 1)
                c_rand = random.randint(0, len(matMons[l_rand]) - 1)
                tiro_M = Sprite("./sprites/bullet.png")
                tiro_especial = Sprite("./sprites/bulletP.png")
                tiro_especial.set_position(matMons[l_rand][c_rand].x + matMons[l_rand][c_rand].width/2, matMons[l_rand][c_rand].y - tiro_M.height)
                tiro_M.set_position(matMons[l_rand][c_rand].x + matMons[l_rand][c_rand].width/2, matMons[l_rand][c_rand].y - tiro_M.height)
                if (paralisar%3 != 0): 
                    mtiro.append(tiro_M)
                elif (paralisar%3 == 0):
                    mtiro.append(tiro_especial)
                tiro_monstro = 0
                paralisar += 1
        for i in range(len(mtiro)):
            mtiro[i].move_y((vel_tiro_m * dificuldade) * gamewindow.delta_time())
            if mtiro[i].y > gamewindow.height - mtiro[i].height:
                mtiro.pop(i)
                break
        
        #Barra de vida
        for i in range(len(mtiro)):
            if not is_immortal and (mtiro[i].collided(player)):
                if(mtiro[i] == tiro_especial):
                    Parar = True
                    Parar_start_time = time.time()
                    vel_player = 0
                    mtiro.pop()
                else:
                    is_immortal = True
                    immortal_start_time = time.time()
                    vet_vida.pop()
                    mtiro.pop()
                    player = Sprite("./sprites/player_imortal.png")
                    player.set_position(gamewindow.width/2 - player.width/2, (gamewindow.height - player.height) - 10)
            #imortal por 2 segundos
            if is_immortal:
                timePass = time.time() - immortal_start_time
                if timePass >= 2:
                    player_x = player.x
                    player_y = player.y
                    player = Sprite("./sprites/player.png")
                    player.set_position(player_x, player_y)

                    is_immortal = False
                        

                

            if len(vet_vida) == 0:
                file = open('Ranking.txt','a+')
                n = str(input())
                file.write('{} = {}\n'.format(n, pontos))
                file.close()
                gamewindow.close()

        #Monstro
        leftmost = matMons[0][0]
        rightmost = matMons[-1][-1]
        bottom = matMons[-1][-1]
        for row in matMons:
            for monster in row:
                if(monster.x < leftmost.x):
                    leftmost = monster
                elif (monster.x > rightmost.x):
                    rightmost = monster
                elif (monster.y > bottom.y):
                    bottom = monster    

        for i in range(len(matMons)):
            for j in range(len(matMons[i])):
                matMons[i][j].move_x((monsVel * dificuldade) * gamewindow.delta_time())

        if leftmost.x < 0:
            monsVel *= -1
            deltax = -leftmost.x
            for i in range(len(matMons)):
                    for j in range(len(matMons[i])):
                        matMons[i][j].set_position(
                            matMons[i][j].x + 2 * deltax,
                            matMons[i][j].y + matMons[i][j].height
                        )

        elif rightmost.x + rightmost.width > gamewindow.width:
            monsVel *= -1
            deltax = (rightmost.x + rightmost.width) - gamewindow.width
            for i in range(len(matMons)):
                    for j in range(len(matMons[i])):
                        matMons[i][j].set_position(
                            matMons[i][j].x - 2 * deltax,
                            matMons[i][j].y + matMons[i][j].height
                        )
                        
        if matMons[-1][-1].y + matMons[-1][-1].height >=  (gamewindow.height - player.height) - 10:
            file = open('Ranking.txt','a+')
            n = str(input())
            file.write('{} = {}\n'.format(n, pontos))
            file.close()
            gamewindow.close()
            
        # Colisao
        new_vtiro = []

        for tiro in vtiro:
            colidir = False
            for linha in matMons:
                if colidir:
                    break
                for monster in linha:
                    if tiro.collided(monster):
                        linha.remove(monster)
                        pontos += 1
                        colidir = True
                        break
            if not colidir:
                new_vtiro.append(tiro)

        vtiro = new_vtiro
        matMons = [row for row in matMons if row]


                            
        # Movimento player
        if Parar:
                timePass = time.time() - Parar_start_time
                if timePass >= 2:
                    vel_player = 200
                    Parar = False
        player.move_key_x(vel_player * gamewindow.delta_time())

        if player.x < 0:
            player.x = 0
        elif player.x > gamewindow.width - player.width:
            player.x = gamewindow.width - player.width

        fundo.draw()
        player.draw()
        for i in range(len(vtiro)):
            vtiro[i].draw()
        for i in range(len(mtiro)):
            mtiro[i].draw()
        for i in range(len(matMons)):
            for j in range(len(matMons[i])):
               matMons[i][j].draw()

        for i in range(len(vet_vida)):
            vet_vida[i].draw()
        
        gamewindow.draw_text("FPS : {} ".format(int(fps)), 20, 10, size=20, color=(255,255,255), font_name="Arial", bold=False, italic=False)
        gamewindow.draw_text("Pontos: {} ".format(pontos), 20, 25, size=20, color=(255,255,255), font_name="Arial", bold=False, italic=False)
        
        
        gamewindow.update()