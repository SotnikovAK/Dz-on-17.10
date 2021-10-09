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
GREY = (127,127,127)
WHITE = (255,255,255)
Color_of_gift = (108,155,190)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

coordinates_button_play = [350,400,100,100]
coordinates_best_score_play = [300,500,200,100]
coordinates_button_esc = [500,0,300,100,600,25]
coordinates_button_play_continue = [100,750,600,50]


coordinates_of_gift_1 = [(69,-72),(52,-93),(-42,-103),(-63,-92),(-77,-85),(0,0)]
coordinates_of_gift_2 = [(94,-74),(100,-87),(79,-102),(46,-117),(-59,-113),(-78,-108),(-99,-87),(-98,-73),(0,0)]

Number_of_enemies_on_levels = [[0,0,0,0],[15,0,0,0],[12,5,1,randint(0,1)],[20,5,5,1],[20,5,15,2]]
Difficult = [[0,0,0,0],[1,0,0,0],[2,3,2,6],[3,3,2,6],[1,2,1,6]]
Score = [1,2,-5,10]

def third_enemy(x,y,R,color):
    circle(screen,color,(x,y),R)
    line(screen,color,(x-1.5*R,y),(x+1.5*R,y),5)
    line(screen,color,(x,y+1.5*R),(x,y-1.5*R),5)
def fourth_enemy(x,y,n, color, color2):
    X,Y=[],[]
    assistant_for_polygon(x,y,X,Y,n,coordinates_of_gift_2)
    polygon(screen, color , [(X[0],Y[0]),(X[1],Y[1]),(X[2],Y[2]),(X[3],Y[3]),(X[4],Y[4]),(X[5],Y[5]),(X[6],Y[6]),(X[7],Y[7]),(X[8],Y[8])],0)
    polygon(screen, color2 , [(X[0],Y[0]),(X[1],Y[1]),(X[2],Y[2]),(X[3],Y[3]),(X[4],Y[4]),(X[5],Y[5]),(X[6],Y[6]),(X[7],Y[7]),(X[8],Y[8])],1)
    X2,Y2=[],[]
    assistant_for_polygon(x,y,X2,Y2,n,coordinates_of_gift_1)
    polygon(screen, color , [(X2[0],Y2[0]),(X2[1],Y2[1]),(X2[2],Y2[2]),(X2[3],Y2[3]),(X2[4],Y2[4]),(X2[5],Y2[5])],0)
    polygon(screen, color2 , [(X2[0],Y2[0]),(X2[1],Y2[1]),(X2[2],Y2[2]),(X2[3],Y2[3]),(X2[4],Y2[4]),(X2[5],Y2[5])],1)

    line(screen,color2,(X2[0],Y2[0]),(X[1],Y[1]),1)
    line(screen,color2,(X2[1],Y2[1]),(X[3],Y[3]),1)
    line(screen,color2,(X2[2],Y2[2]),(X[4],Y[4]),1)
    line(screen,color2,(X2[4],Y2[4]),(X[6],Y[6]),1)

def coordinates_new_enemy(class_of_enemy):
    XY_R_color = []
    XY_R_color.append(randint(200,600))
    XY_R_color.append(randint(250,700))
    XY_R_color.append(randint(10,20))
    color = COLORS[randint(0, 5)]
    if class_of_enemy == 1:
        circle(screen, color, (XY_R_color[0], XY_R_color[1]), XY_R_color[2])
        cost_of_enemy = 1
        XY_R_color.append(color)
    elif class_of_enemy == 2:
        rect(screen, color, (XY_R_color[0], XY_R_color[1],XY_R_color[2], XY_R_color[2]))
        cost_of_enemy = 2
        XY_R_color.append(color)
    elif class_of_enemy == 3:
        third_enemy(XY_R_color[0], XY_R_color[1], XY_R_color[2],color)
        cost_of_enemy = -5
        XY_R_color.append(color)
    else:
        fourth_enemy(XY_R_color[0], XY_R_color[1], XY_R_color[2] / 5, Color_of_gift , BLACK)
        cost_of_enemy = 10
        XY_R_color.append(Color_of_gift)

    XY_R_color.append(class_of_enemy)
    XY_R_color.append(cost_of_enemy)
    XY_R_color.append(BLACK)
    return XY_R_color

def speeds_new_enemy(n):
    
    V = []
    V.append(randint(-n,n))
    V.append(randint(-n,n))
    return V

def examination(x,y,A):
    if (A[4] == 1 or A[4] == 3):
        square_r = (A[0]-x)*(A[0]-x) + (A[1]-y)*(A[1]-y)
        if (A[2] * A[2] >= square_r):
            if (abs(x-A[0])<= A[2] and abs(y-A[1])<= A[2] ):
                return 1
            else:
                return 0
        else:
            return 0
    elif (A[4] == 2):
        if ((A[0]<=x and x-A[0] <= A[2]) and (A[1]<=y and y-A[1]<=A[2]) ):
            return 1
        else:
            return 0
    else:
        if (abs(A[0]-x) <= 100 / A[2] * 5) and (A[1] - 120/A[2]* 5 <= y and y<=A[1]):
            return 1
        else:
            return 0

def move_balls():
    for i in range(number_of_enemies):
        random_coord = [randint(100,700),randint(150,800)]
        for j in range(2):
            if (coordinates_new_enemies[i][4] != 4):
                if ((coordinates_new_enemies[i][j] + speed_new_enemies[i][j] >= LIMIT_moves[j+2] - coordinates_new_enemies[i][2]) or  (LIMIT_moves[j] + coordinates_new_enemies[i][2] >= coordinates_new_enemies[i][j] + speed_new_enemies[i][j])):
                    coordinates_new_enemies[i][j] = random_coord[j]
                else:
                    coordinates_new_enemies[i][j] += speed_new_enemies[i][j]
            else :
                if ((coordinates_new_enemies[i][j] + speed_new_enemies[i][j] >= LIMIT_moves_gift[j+2] - coordinates_new_enemies[i][2]) or  (LIMIT_moves_gift[j] + coordinates_new_enemies[i][2] >= coordinates_new_enemies[i][j] + speed_new_enemies[i][j])):
                    coordinates_new_enemies[i][j] = random_coord[j]
                else:
                    coordinates_new_enemies[i][j] += speed_new_enemies[i][j]
        if coordinates_new_enemies[i][4] == 1:
            circle(screen, coordinates_new_enemies[i][3] , (coordinates_new_enemies[i][0], coordinates_new_enemies[i][1]), coordinates_new_enemies[i][2])

        elif coordinates_new_enemies[i][4] == 2:
            rect(screen,coordinates_new_enemies[i][3], (coordinates_new_enemies[i][0], coordinates_new_enemies[i][1],coordinates_new_enemies[i][2],coordinates_new_enemies[i][2]))
        elif coordinates_new_enemies[i][4] == 3:
            third_enemy(coordinates_new_enemies[i][0], coordinates_new_enemies[i][1], coordinates_new_enemies[i][2],coordinates_new_enemies[i][3])
        else:
            fourth_enemy(coordinates_new_enemies[i][0], coordinates_new_enemies[i][1],coordinates_new_enemies[i][2]/5, coordinates_new_enemies[i][3] ,coordinates_new_enemies[i][6])
def exterminatus_of_balls():
    for i in range(len(fl)):
        if (fl[i] == 1):
            coordinates_new_enemies[i][3] = GREY
            coordinates_new_enemies[i][6] = GREY
            if coordinates_new_enemies[i][4] != 4:
                coordinates_new_enemies[i][2] = 0
    
def background(flag):
    rect(screen, GREY , (0,100,800,900))
    if (flag == 0):
        battle_ground()
    elif (flag == 4):
        menu_of_game()
    elif (flag == 5):
        best_score_screen()
    elif (flag == 3):
        loading_screen()
    elif (flag == 2):
        after_lavel_background()
    rect(screen, BLACK , (0,0,800,900), 5)

def menu_of_game():
    rect(screen, GREY , (0,0,800,100))

    rect(screen, WHITE, (100,50,600,100))
    rect(screen, BLACK, (100,50,600,100),5)
    text(200,75,'Catch the BALL!', BLACK, 64)

    rect(screen, WHITE, coordinates_button_play)
    rect(screen, BLACK, coordinates_button_play,5)
    text(355,425,'PLAY!', RED , 45)

    rect(screen, WHITE, coordinates_best_score_play)
    rect(screen, BLACK, coordinates_best_score_play, 5)
    text(325,525,'Best Score ', BLACK , 45)

def best_score_screen():
    rect(screen, GREY , (0,0,800,100))

    button_esc()
    
def loading_screen():
    rect(screen, GREY , (0,0,800,100))
    rect(screen, WHITE ,coordinates_button_play_continue)
    if loading_bar <= 600:
        rect(screen, GREEN, (100,750,loading_bar,50))
        rect(screen, BLACK,coordinates_button_play_continue,5)
    else:
        rect(screen, RED ,coordinates_button_play_continue)
        text(300,750,'Continue', BLACK , 64)
        rect(screen, BLACK,coordinates_button_play_continue,5)
    rules()
    rect(screen, BLACK,coordinates_button_play_continue,5)
def rules():
    rect(screen,WHITE,(200,100,400,600))
    text(325,100,'Rules',BLACK, 64)
    rect(screen, BLACK, (200,150,400,0),5)
    
    circle(screen, YELLOW , (275,225),40)
    text(325,200,' = ', BLACK,64)
    text(375,200,' +1 point ', BLACK,64)

    rect(screen, BLUE, (250,300,60,60))
    text(325,300,' = ', BLACK,64)
    text(375,300,' +2 point ', BLACK,64)

    third_enemy(275,425,25,RED)
    text(325,400,' = ', BLACK,64)
    text(375,400,' -5 point ', BLACK,64)

    fourth_enemy(275,550,2,Color_of_gift,BLACK)
    text(325,500,' = ', BLACK,64)
    text(375,500,' +10 point ', BLACK,64)
    
    rect(screen,BLACK,(200,100,400,600),5)
def after_lavel_background():
    rect(screen, GREY , (0,0,800,100))
    rect(screen,WHITE,(100,100,600,500))
    rect(screen,BLACK,(100,100,600,500),5)

    line(screen, BLACK ,(100,350),(700,350),5)
    text(225,200,'Progress:',BLACK , 64)
    text(525,200, str(score) + ' / ' + str(MAX_score),BLACK, 64)
    line(screen, BLACK ,(500,100),(500,600),5)
    text(225,450,'Grade:',BLACK , 64)

    rect(screen, RED ,coordinates_button_play_continue)
    text(300,750,'Continue', BLACK , 64)
    rect(screen, BLACK,coordinates_button_play_continue,5)
def score_table(score):
    text(50,25,'Score: ' + str(score),BLACK,64)
    line(screen, BLACK, (275,0), (275,100) ,5 )

def button_esc():
    rect(screen, RED , (coordinates_button_esc[0],coordinates_button_esc[1],coordinates_button_esc[2],coordinates_button_esc[3]),0)
    rect(screen, BLACK , (coordinates_button_esc[0],coordinates_button_esc[1],coordinates_button_esc[2],coordinates_button_esc[3]),5)
    text(coordinates_button_esc[4],coordinates_button_esc[5],'Quit', BLACK, 64)

def battle_ground():
    rect(screen, WHITE, (0,0,800,100))
    line(screen, BLACK , (0,100), (800,100), 5)



def button(x,y,coordinates):
    if (x >= coordinates[0] and x <= coordinates[0] + coordinates[2] and y >= coordinates[1] and y <= coordinates[1] + coordinates[3]):
        return 1
    return 0

def text(x,y,A,color,size):
    pygame.font.init()
    myfont = pygame.font.SysFont(' ', size)
    textsurface = myfont.render(A ,False, color)
    screen.blit(textsurface,(x,y))

def assistant_for_polygon(x,y,X,Y,n,coordinates):

    for i in range(len(coordinates)):
        X.append(coordinates[i][0]/n + x)
        Y.append(coordinates[i][1]/n + y)
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

LIMIT_moves = [0,100,800,900]
LIMIT_moves_gift = [100,200,700,800]

score = 0
time_of_life_game = 0
flag = 4

loading_bar =  100
flag_loading_screen =  1

while not finished:
    clock.tick(FPS)
    background(flag)
    T = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if (flag == 4):

                Level = 1

                if (button(event.pos[0], event.pos[1],coordinates_button_play) == 1):
                    flag = 3

                elif (button(event.pos[0], event.pos[1],coordinates_best_score_play) == 1 ):
                    flag = 5

            elif (flag == 0):
                if (button(event.pos[0], event.pos[1],coordinates_button_esc) == 1):
                    flag = 4
                else: 
                    fl = []
                    for i in range(number_of_enemies):
                        fl.append(examination(event.pos[0], event.pos[1], coordinates_new_enemies[i]))
                        score += (examination(event.pos[0], event.pos[1], coordinates_new_enemies[i]) * coordinates_new_enemies[i][5] )
                    exterminatus_of_balls()
        
            elif (flag == 5):

                if (button(event.pos[0], event.pos[1],coordinates_button_esc) == 1):
                    flag = 4

            elif (flag == 3):

                if (button(event.pos[0], event.pos[1],coordinates_button_play_continue) == 1 and flag_loading_screen == 0):
                    flag = 0
                    loading_bar = 100
                    flag_loading_screen == 1
            elif (flag == 2):
                score = 0
                if (button(event.pos[0], event.pos[1],coordinates_button_play_continue) == 1 and flag_loading_screen == 0):
                    flag = 0
                
        if (flag == 3):
            if (loading_bar >= 600):
                flag_loading_screen =  0
            loading_bar += 20
            

    if (flag == 0):   
        if (time_of_life_game%1000 == 0):
            if  Level == 5:
                break
            number_of_enemies_on_current_level = Number_of_enemies_on_levels[Level]
            difficult_of_enemies_on_current_level = Difficult[Level]

            coordinates_new_enemies =[]
            speed_new_enemies = []

            number_of_enemies = 0
            MAX_score = 0

            for i in range(4) :
                if (number_of_enemies_on_current_level[i] != 0):
                        for j in range(number_of_enemies_on_current_level[i]):
                            coordinates_new_enemies.append(coordinates_new_enemy(i+1))
                            speed_new_enemies.append(speeds_new_enemy(difficult_of_enemies_on_current_level[i]))
                MAX_score += Score[i] * number_of_enemies_on_current_level[i]  
                number_of_enemies += number_of_enemies_on_current_level[i]

            Level += 1


        else:
            move_balls()

        score_table(score)
        button_esc()
        time_of_life_game += 1
    
    pygame.display.update()

pygame.quit()