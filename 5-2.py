import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 100
screen = pygame.display.set_mode((800, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)
Color_of_gift = (108, 155, 190)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

coordinates_button_play = [300, 400, 200, 100]
coordinates_button_infinite_play = [300, 500, 200, 100]
coordinates_button_esc = [500, 0, 300, 100, 600, 25]
coordinates_button_play_continue = [100, 750, 600, 50]
coordinates_button_save_score = [100, 650, 600, 50]

coordinates_of_gift_1 = [(69, -72), (52, -93),
                         (-42, -103), (-63, -92), (-77, -85), (0, 0)]
coordinates_of_gift_2 = [(94, -74), (100, -87), (79, -102), (46, -117),
                         (-59, -113), (-78, -108), (-99, -87), (-98, -73), (0, 0)]

Number_of_enemies_on_levels = [[0, 0, 0, 0], [15, 0, 0, 0], [
    12, 5, 1, randint(0, 1)], [20, 5, 5, 1], [20, 5, 15, 2]]
Difficult = [[0, 0, 0, 0], [1, 0, 0, 0], [
    2, 3, 2, 6], [3, 3, 2, 6], [1, 2, 1, 6]]
Score = [1, 2, -5, 10]
BEST_SCORE = [0] * 13
PlAYER_NAME = [0] * 13

#ENEMIES
def third_enemy(x, y, R, color):
    circle(screen, color, (x, y), R)
    line(screen, color, (x-1.5*R, y), (x+1.5*R, y), 5)
    line(screen, color, (x, y+1.5*R), (x, y-1.5*R), 5)

def fourth_enemy(x, y, n, color, color2):
    X, Y = [], []
    assistant_for_polygon(x, y, X, Y, n, coordinates_of_gift_2)
    polygon(screen, color, [(X[0], Y[0]), (X[1], Y[1]), (X[2], Y[2]), (X[3], Y[3]), (
        X[4], Y[4]), (X[5], Y[5]), (X[6], Y[6]), (X[7], Y[7]), (X[8], Y[8])], 0)
    polygon(screen, color2, [(X[0], Y[0]), (X[1], Y[1]), (X[2], Y[2]), (X[3], Y[3]), (
        X[4], Y[4]), (X[5], Y[5]), (X[6], Y[6]), (X[7], Y[7]), (X[8], Y[8])], 1)
    X2, Y2 = [], []
    assistant_for_polygon(x, y, X2, Y2, n, coordinates_of_gift_1)
    polygon(screen, color, [(X2[0], Y2[0]), (X2[1], Y2[1]), (X2[2],
            Y2[2]), (X2[3], Y2[3]), (X2[4], Y2[4]), (X2[5], Y2[5])], 0)
    polygon(screen, color2, [(X2[0], Y2[0]), (X2[1], Y2[1]), (X2[2],
            Y2[2]), (X2[3], Y2[3]), (X2[4], Y2[4]), (X2[5], Y2[5])], 1)

    line(screen, color2, (X2[0], Y2[0]), (X[1], Y[1]), 1)
    line(screen, color2, (X2[1], Y2[1]), (X[3], Y[3]), 1)
    line(screen, color2, (X2[2], Y2[2]), (X[4], Y[4]), 1)
    line(screen, color2, (X2[4], Y2[4]), (X[6], Y[6]), 1)

def coordinates_new_enemy(class_of_enemy):
    XY_R_color = []
    XY_R_color.append(randint(200, 600))
    XY_R_color.append(randint(250, 700))
    XY_R_color.append(randint(10, 20))
    color = COLORS[randint(0, 5)]
    if class_of_enemy == 1:
        circle(screen, color, (XY_R_color[0], XY_R_color[1]), XY_R_color[2])
        cost_of_enemy = 1
        XY_R_color.append(color)
    elif class_of_enemy == 2:
        rect(screen, color,
             (XY_R_color[0], XY_R_color[1], XY_R_color[2], XY_R_color[2]))
        cost_of_enemy = 2
        XY_R_color.append(color)
    elif class_of_enemy == 3:
        third_enemy(XY_R_color[0], XY_R_color[1], XY_R_color[2], color)
        cost_of_enemy = -5
        XY_R_color.append(color)
    else:
        fourth_enemy(XY_R_color[0], XY_R_color[1],
                     XY_R_color[2] / 5, Color_of_gift, BLACK)
        cost_of_enemy = 10
        XY_R_color.append(Color_of_gift)

    XY_R_color.append(class_of_enemy)
    XY_R_color.append(cost_of_enemy)
    XY_R_color.append(BLACK)
    return XY_R_color

def speeds_new_enemy(n,i):

    V = []
    if i!= 1:
        Vx = randint(-n, n) + randint(-n, n) / 10
        Vy = randint(-n, n) + randint(-n, n) / 10
        if (Vx == 0):
            VX = n
        if (Vy == 0):
            Vy = n
    else:
        if (randint(0,1) == 1):
            Vx = 0
            Vy = randint(-n, n) + randint(-n, n) / 10
        else:
            Vx = randint(-n, n) + randint(-n, n) / 10
            Vy = 0
    V.append(Vx)
    V.append(Vy)
    return V

def examination(x, y, A):
    if (A[4] == 1 or A[4] == 3):
        square_r = (A[0]-x)*(A[0]-x) + (A[1]-y)*(A[1]-y)
        if (A[2] * A[2] >= square_r):
            if (abs(x-A[0]) <= A[2] and abs(y-A[1]) <= A[2]):
                return 1
            else:
                return 0
        else:
            return 0
    elif (A[4] == 2):
        if ((A[0] <= x and x-A[0] <= A[2]) and (A[1] <= y and y-A[1] <= A[2])):
            return 1
        else:
            return 0
    else:
        if (abs(A[0]-x) <= 100 / A[2] * 5) and (A[1] - 120/A[2] * 5 <= y and y <= A[1]):
            return 1
        else:
            return 0

def move_balls():
    for i in range(number_of_enemies):
        random_coord = [randint(100, 700), randint(150, 800)]
        for j in range(2):
            if (coordinates_new_enemies[i][4] != 4):
                if ((coordinates_new_enemies[i][j] + speed_new_enemies[i][j] >= LIMIT_moves[j+2] - coordinates_new_enemies[i][2]) or (LIMIT_moves[j] + coordinates_new_enemies[i][2] >= coordinates_new_enemies[i][j] + speed_new_enemies[i][j])):
                    coordinates_new_enemies[i][j] = random_coord[j]
                else:
                    coordinates_new_enemies[i][j] += speed_new_enemies[i][j]
            else:
                if ((coordinates_new_enemies[i][j] + speed_new_enemies[i][j] >= LIMIT_moves_gift[j+2] - coordinates_new_enemies[i][2]) or (LIMIT_moves_gift[j] + coordinates_new_enemies[i][2] >= coordinates_new_enemies[i][j] + speed_new_enemies[i][j])):
                    coordinates_new_enemies[i][j] = random_coord[j]
                else:
                    coordinates_new_enemies[i][j] += speed_new_enemies[i][j]
        if coordinates_new_enemies[i][4] == 1:
            circle(screen, coordinates_new_enemies[i][3], (coordinates_new_enemies[i]
                   [0], coordinates_new_enemies[i][1]), coordinates_new_enemies[i][2])

        elif coordinates_new_enemies[i][4] == 2:
            rect(screen, coordinates_new_enemies[i][3], (coordinates_new_enemies[i][0],
                 coordinates_new_enemies[i][1], coordinates_new_enemies[i][2], coordinates_new_enemies[i][2]))
        elif coordinates_new_enemies[i][4] == 3:
            third_enemy(coordinates_new_enemies[i][0], coordinates_new_enemies[i]
                        [1], coordinates_new_enemies[i][2], coordinates_new_enemies[i][3])
        else:
            fourth_enemy(coordinates_new_enemies[i][0], coordinates_new_enemies[i][1],
                         coordinates_new_enemies[i][2]/5, coordinates_new_enemies[i][3], coordinates_new_enemies[i][6])

def exterminatus_of_balls():
    n = 0
    for i in range(len(fl)):
        if (fl[i] == 1):
            n += 1
            coordinates_new_enemies[i][3] = GREY
            coordinates_new_enemies[i][6] = GREY
            if coordinates_new_enemies[i][4] != 4:
                coordinates_new_enemies[i][2] = 0
    return n

def generation(n,MAX_score,number_of_enemies):
    for i in range(n):
        if (number_of_enemies_on_current_level[i] != 0):
            for j in range(number_of_enemies_on_current_level[i]):
                coordinates_new_enemies.append(coordinates_new_enemy(i+1))
                speed_new_enemies.append(speeds_new_enemy(difficult_of_enemies_on_current_level[i],i))
        if i!=2 :
            MAX_score += Score[i] * number_of_enemies_on_current_level[i]
        number_of_enemies += number_of_enemies_on_current_level[i]
    return MAX_score,number_of_enemies

def rules_spawn_endless_gamemode_at_first_time():
    number_of_enemies_on_current_level = [0] * 4
    difficult_of_enemies_on_current_level = [0] * 4

    for i in range(2):
        number_of_enemies_on_current_level[i] = randint(25,30)
        difficult_of_enemies_on_current_level[i] = randint(i+1,i+2)
            
    number_of_enemies_on_current_level[2] = 0
    difficult_of_enemies_on_current_level[2] = 0

    number_of_enemies_on_current_level[3] = 0
    difficult_of_enemies_on_current_level[3] = 0

    return number_of_enemies_on_current_level, difficult_of_enemies_on_current_level

def rules_spawn_endless_gamemode_in_progress_game():
    number_of_enemies_on_current_level = [0] * 4
    difficult_of_enemies_on_current_level = [0] * 4
    n = randint(0,1)
    difficult_of_enemies_on_current_level[n] = randint(1,3)
    number_of_enemies_on_current_level[n] = 1

    return number_of_enemies_on_current_level, difficult_of_enemies_on_current_level


#background
def background(flag):
    rect(screen, GREY, (0, 100, 800, 900))
    if (flag == 0):
        battle_ground()
    elif (flag == 4):
        menu_of_game()
    elif (flag == 5):
        best_score_screen()
    elif (flag == 3):
        loading_screen()
    elif (flag == 2):
        after_level_background()
    elif (flag == -1):
        error_loading_screen()
    elif (flag == 1):
        screen_of_finish_infinite_game()

    elif (flag == 6):
        #don't work
        screen_of_finish_infinite_game()
        screen_of_input_name_player()

    rect(screen, BLACK, (0, 0, 800, 900), 5)

def menu_of_game():
    rect(screen, GREY, (0, 0, 800, 100))

    rect(screen, WHITE, (100, 50, 600, 100))
    rect(screen, BLACK, (100, 50, 600, 100), 5)
    text(200, 75, 'Catch the BALL!', BLACK, 64)

    rect(screen, WHITE, coordinates_button_play)
    rect(screen, BLACK, coordinates_button_play, 5)
    text(325, 425, 'Campaign', RED, 40)

    rect(screen, WHITE, coordinates_button_infinite_play)
    rect(screen, BLACK, coordinates_button_infinite_play, 5)
    text(310, 525, 'Endless game ', BLUE , 40)

    rect(screen, WHITE, coordinates_button_play_continue)
    text(225, 760, 'Best players of Endless game' , BLACK, 40)
    rect(screen, BLACK, coordinates_button_play_continue, 5)

def best_score_screen(): # Here i must do read from file , while i don't make it for simplicity + I must make input of name from klava 
    
    rect(screen, GREY, (0, 0, 800, 100))
    rect(screen, WHITE, (100,125,600,700))
    rect(screen, BLACK, (100,125,600,700),5)

    line(screen, BLACK, (200,125),(200,700+125),5)
    line(screen, BLACK, (550,125),(550,125+700),5)

    text(563,137,'SCORE:',BLACK, 40)
    text(273,137,'Name player:',BLACK, 40)
    text(113,137,'Place',BLACK,40 )

    delta = 1
    for i in range(175,125+700,50):
        line(screen,BLACK, (100,i),(700,i),5)
        text(113,137+delta * 50,(str(delta) + '.'),BLACK,40 )
        if PlAYER_NAME[delta-1] != 0:
            text(273,137 + delta * 50,'PLAYER-' + str(PlAYER_NAME[delta-1]) ,BLACK, 40)
            text(563,137 + delta * 50, str(BEST_SCORE[delta-1]),BLACK, 40)
        delta += 1
    button_esc()

def loading_screen():
    rect(screen, GREY, (0, 0, 800, 100))
    rect(screen, WHITE, coordinates_button_play_continue)
    if loading_bar <= 600:
        rect(screen, GREEN, (100, 750, loading_bar, 50))
        rect(screen, BLACK, coordinates_button_play_continue, 5)
    else:
        rect(screen, RED, coordinates_button_play_continue)
        text(300, 750, 'Continue', BLACK, 64)
        rect(screen, BLACK, coordinates_button_play_continue, 5)
    rules()
    rect(screen, BLACK, coordinates_button_play_continue, 5)

def rules():
    rect(screen, WHITE, (200, 100, 400, 600))
    text(325, 100, 'Rules', BLACK, 64)
    rect(screen, BLACK, (200, 150, 400, 0), 5)

    circle(screen, YELLOW, (275, 225), 40)
    text(325, 200, ' = ', BLACK, 64)
    text(375, 200, ' +1 point ', BLACK, 64)

    rect(screen, BLUE, (250, 300, 60, 60))
    text(325, 300, ' = ', BLACK, 64)
    text(375, 300, ' +2 point ', BLACK, 64)
    if endless_game_mode == 0:
        third_enemy(275, 425, 25, RED)
        text(325, 400, ' = ', BLACK, 64)
        text(375, 400, ' -5 point ', BLACK, 64)

        fourth_enemy(275, 550, 2, Color_of_gift, BLACK)
        text(325, 500, ' = ', BLACK, 64)
        text(375, 500, ' +10 point ', BLACK, 64)
    else:
        text(225, 400, ' If the number of enemies ', BLACK, 40)
        text(225, 450,' exceeds 100, you lose .', BLACK, 40)
    rect(screen, BLACK, (200, 100, 400, 600), 5)

def after_level_background():
    rect(screen, GREY, (0, 0, 800, 100))
    rect(screen, WHITE, (100, 100, 600, 500))
    rect(screen, BLACK, (100, 100, 600, 500), 5)

    line(screen, BLACK, (100, 350), (700, 350), 5)
    text(225, 200, 'Progress:', BLACK, 64)
    text(525, 200, str(p) + ' / ' + str(MAX_score), BLACK, 64)
    line(screen, BLACK, (500, 100), (500, 600), 5)
    text(225, 450, 'Grade:', BLACK, 64)
    A = ()
    w = (p / MAX_score * 100)//1
    if (w < 30):
        A = ('НЕУД/' + str(int(w)//10))
    elif (30 <= w and w < 50):
        A = ('УД/' + str(int(w)//10))
    elif (50 <= w and w < 80):
        A = ('ХОР/' + str(int(w)//10))
    else:
        A = ('ОТЛ/' + str(int(w)//10))
    text(525, 450, A , BLACK, 64)
    rect(screen, RED, coordinates_button_play_continue)
    text(300, 750, 'Continue', BLACK, 64)
    rect(screen, BLACK, coordinates_button_play_continue, 5)

def error_loading_screen():

    rect(screen, GREY, (0, 0, 800, 100))
    rect(screen, WHITE, coordinates_button_infinite_play)
    rect(screen, BLACK, coordinates_button_infinite_play, 5)
    text(310, 525, 'You Should Complete Campaign', RED, 16)

def score_table(score):
    text(50, 25, 'Score: ' + str(score), BLACK, 64)
    line(screen, BLACK, (275, 0), (275, 100), 5)

def screen_of_input_name_player():#don't work
    rect(screen, GREY, (70, 270, 660, 200))
    rect(screen, BLACK, (70, 270, 660, 200), 5)

    rect(screen, WHITE, (130, 330, 540, 80))
    rect(screen, BLACK, (130, 330, 540, 80), 5)

def screen_of_finish_infinite_game():
    rect(screen, GREY, (0, 0, 800, 100))
    rect(screen, WHITE, (100, 100, 600, 250))
    rect(screen, BLACK, (100, 100, 600, 250), 5)

    line(screen, BLACK, (100, 350), (700, 350), 5)
    text(225, 200, 'Score:', BLACK, 64)
    text(525, 200, str(p) , BLACK, 64)

    rect(screen, GREEN, coordinates_button_save_score)
    text(300, 650, 'Save score', BLACK, 64)
    rect(screen, BLACK, coordinates_button_save_score, 5)

    rect(screen, RED, coordinates_button_play_continue)
    text(350, 750, 'Exit', BLACK, 64)
    rect(screen, BLACK, coordinates_button_play_continue, 5)

def button_esc():
    rect(screen, RED, (coordinates_button_esc[0], coordinates_button_esc[1],
         coordinates_button_esc[2], coordinates_button_esc[3]), 0)
    rect(screen, BLACK, (coordinates_button_esc[0], coordinates_button_esc[1],
         coordinates_button_esc[2], coordinates_button_esc[3]), 5)
    text(coordinates_button_esc[4],
         coordinates_button_esc[5], 'Quit', BLACK, 64)

def battle_ground():
    rect(screen, WHITE, (0, 0, 800, 100))
    line(screen, BLACK, (0, 100), (800, 100), 5)

#service functions
def button(x, y, coordinates):
    if (x >= coordinates[0] and x <= coordinates[0] + coordinates[2] and y >= coordinates[1] and y <= coordinates[1] + coordinates[3]):
        return 1
    return 0
def text(x, y, A, color, size):
    pygame.font.init()
    myfont = pygame.font.SysFont(' ', size)
    textsurface = myfont.render(A, False, color)
    screen.blit(textsurface, (x, y))
def assistant_for_polygon(x, y, X, Y, n, coordinates):

    for i in range(len(coordinates)):
        X.append(coordinates[i][0]/n + x)
        Y.append(coordinates[i][1]/n + y)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

LIMIT_moves = [0, 100, 800, 900]
LIMIT_moves_gift = [100, 200, 700, 800]

score = 0
time_of_life_game = 0
flag = 4
endless_game_mode = 0
flag_unlock_endless_gamemode = 1

loading_bar = 100
flag_loading_screen = 1


#crutches
number_player = 0


while not finished:
    clock.tick(FPS)

    background(flag)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if (flag == 4): #menu game

                Level = 1
                MAX_score_full = 0
                Score_full = 0

                coordinates_new_enemies = []
                speed_new_enemies = []

                if (button(event.pos[0], event.pos[1], coordinates_button_play) == 1):
                    Level = 1
                    number_of_enemies = 0
                    k = 0
                    endless_game_mode = 0
                    flag = 3
                

                elif (button(event.pos[0], event.pos[1], coordinates_button_play_continue) == 1):
                    flag = 5

                if (button(event.pos[0], event.pos[1], coordinates_button_infinite_play) == 1):
                    number_of_enemies = 0
                    k = 0
                    time_of_life_game = 0
                    if (flag_unlock_endless_gamemode == 1):
                        endless_game_mode = 1
                        flag = 3
                    else:
                        flag = -1
            elif (flag == 0): #welcome to the battle zone

                if (button(event.pos[0], event.pos[1], coordinates_button_esc) == 1):
                    if endless_game_mode == 0:
                        flag = 4
                    elif (endless_game_mode == 1):
                        p = score
                        flag = 1

                    score = 0
                    Level = 1
                    number_of_enemies = 0
                    k = 0
                    endless_game_mode = 0
                    
                else:
                    fl = []
                    for i in range(number_of_enemies):
                        fl.append(examination(
                            event.pos[0], event.pos[1], coordinates_new_enemies[i]))
                        score += (examination(event.pos[0], event.pos[1],
                                  coordinates_new_enemies[i]) * coordinates_new_enemies[i][5])
                    k += exterminatus_of_balls()
            elif (flag == 5): #best score screen

                if (button(event.pos[0], event.pos[1], coordinates_button_esc) == 1):
                    flag = 4
            elif (flag == 3): #screen of loading game

                if (button(event.pos[0], event.pos[1], coordinates_button_play_continue) == 1 and flag_loading_screen == 0):
                    flag = 0
                    loading_bar = 100
                    flag_loading_screen == 1
            elif (flag == 2): #screen finish campaign level

                score = 0
                number_of_enemies = 0
                k = 0
                coordinates_new_enemies = []
                speed_new_enemies = []

                if (button(event.pos[0], event.pos[1], coordinates_button_play_continue) == 1 and flag_loading_screen == 0):
                    flag = 0
            elif (flag == 1 ): #screen of finish infinte game

                if (button(event.pos[0], event.pos[1], coordinates_button_play_continue) == 1 ):
                    flag = 4
                
                if (button(event.pos[0], event.pos[1], coordinates_button_save_score) == 1 ):

                    BEST_SCORE.append(p)
                    number_player += 1
                    PlAYER_NAME.append(number_player)

                    for i in range(len(BEST_SCORE)):
                        for j in range(len(BEST_SCORE) - 1 - i):
                            if BEST_SCORE[j] <= BEST_SCORE[j+1]:
                                BEST_SCORE[j], BEST_SCORE[j+1] = BEST_SCORE[j+1], BEST_SCORE[j]
                                PlAYER_NAME[j], PlAYER_NAME[j+1] = PlAYER_NAME[j+1], PlAYER_NAME[j]

                    flag = 5

            elif (flag == -1 ): #error endless gamemode screen

                if (button(event.pos[0], event.pos[1], coordinates_button_infinite_play) == 1):
                    flag = 4
            
        if (flag == 3):
            if (loading_bar >= 600):
                flag_loading_screen = 0
            loading_bar += 20

    if (flag == 0 and endless_game_mode == 0):
        if (time_of_life_game == 0 ):
            k = 0
            if Level == 5:
                    
                flag_unlock_endless_gamemode = 1
                
                Level = 1

                flag = 4

            number_of_enemies_on_current_level = Number_of_enemies_on_levels[Level]
            difficult_of_enemies_on_current_level = Difficult[Level]

            MAX_score,number_of_enemies = generation(4,0,0)

            Level += 1

        else:
            move_balls()

        score_table(score)
        button_esc()
        time_of_life_game += 1

        if (time_of_life_game == 1500):
            p = score
            Score_full += score
            MAX_score_full += MAX_score
            flag = 2
            time_of_life_game = 0

    elif (endless_game_mode == 1 and flag == 0):

        if ((number_of_enemies - k) <= 60):
            if (time_of_life_game == 0):

                k = 0
                
                number_of_enemies_on_current_level, difficult_of_enemies_on_current_level = rules_spawn_endless_gamemode_at_first_time()

                MAX_score, number_of_enemies = generation(4,0,0)
            elif (time_of_life_game % 100 == 0):
                number_of_enemies_on_current_level, difficult_of_enemies_on_current_level = rules_spawn_endless_gamemode_in_progress_game()

                F, l = generation(4,0,0)
                number_of_enemies += 1

            else:
                move_balls()

            score_table(score)
            button_esc()
            time_of_life_game += 1

        else:
            number_of_enemies_on_current_level = []
            difficult_of_enemies_on_current_level = []

            flag = 1
            p = score
            time_of_life_game = 0
            score = 0

    pygame.display.update()

pygame.quit()

