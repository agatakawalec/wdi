import pygame
import time
import random
random.seed()

pygame.init()
pygame.display.set_caption('Snake')

#KOLORY
pudrowy=(204,102,102)
black=(0,0,0)
green=(0,255,0)

#PEWNE STAŁE
szer=500
wys=500 #na odwrot- ZMIENIC
head_x = szer / 2
head_y = wys / 2
mv_size = 10
FPS = 100
head_x_move = 0
head_y_move = 0
clock = pygame.time.Clock()
direction="right"
zdj=pygame.image.load('head2.png') #waz
zdj1=pygame.image.load('backgroundgra.jpeg') #tlo
zdj2=pygame.image.load('jablko.png') #jablko
zdj3=pygame.image.load('morela.png')
zdj4=pygame.image.load('malina.png')
zdj5=pygame.image.load('orange.png')
pygame.mixer.music.load("Gra o tron.mp3")

display=pygame.display.set_mode((wys,szer))

def pause():
    paused=True
    display.blit(zdj1,(0,0))
    print_msg("Paused",pudrowy,200,100,50)
    print_msg("Press SPACE",pudrowy,225,200,30)
    print_msg("to play", pudrowy, 250, 240, 30)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused=False


def snake(sn_mv):

    if direction=="right":
        head=pygame.transform.rotate(zdj,270)
        display.blit(head, (sn_mv[-1][0], sn_mv[-1][1]))
        for sth in sn_mv[:-1]:
            display.blit(head, (sth[0], sth[1]))

    elif direction=="left":
        head=pygame.transform.rotate(zdj,90)
        display.blit(head, (sn_mv[-1][0], sn_mv[-1][1]))
        for sth in sn_mv[:-1]:
            display.blit(head, (sth[0], sth[1]))

    elif direction=="down":
        head=pygame.transform.rotate(zdj,180)
        display.blit(head, (sn_mv[-1][0], sn_mv[-1][1]))
        for sth in sn_mv[:-1]:
            display.blit(head, (sth[0], sth[1]))

    elif direction=="up":
        head=pygame.transform.rotate(zdj,0)
        display.blit(head, (sn_mv[-1][0], sn_mv[-1][1]))
        for sth in sn_mv[:-1]:
            display.blit(head, (sth[0], sth[1]))

def menu():
    #const
    szerokosc=300
    wysokosc=70
    pygame.mixer.music.play(-1,0.0)
    display.blit(zdj1, (0, 0))
    prost1=pygame.Rect(100,160,szerokosc,wysokosc)
    prost2=pygame.Rect(100,310,szerokosc,wysokosc)
    pygame.draw.rect(display,pudrowy,(100,160,szerokosc,wysokosc))
    pygame.draw.rect(display,pudrowy,(100,310,szerokosc,wysokosc))
    print_msg("SNAKE",pudrowy,185,20,70)
    print_msg("PLAY",black,200,165,40)
    print_msg("QUIT",black,200,315,40)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if prost1.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                time.sleep(0.2)

                display.blit(zdj1, (0, 0))
                print_msg("Get ready!",pudrowy,200,200,30)
                pygame.display.update()
                time.sleep(0.7)

                display.blit(zdj1, (0, 0))
                print_msg("3",pudrowy,249,200,30)
                pygame.display.update()
                time.sleep(0.7)

                display.blit(zdj1, (0, 0))
                print_msg("2",pudrowy,249,200,30)
                pygame.display.update()
                time.sleep(0.7)

                display.blit(zdj1, (0, 0))
                print_msg("1", pudrowy, 249, 200, 30)
                pygame.display.update()
                time.sleep(0.7)

                display.blit(zdj1, (0, 0))
                print_msg("START!", pudrowy, 220, 200, 30)
                pygame.display.update()
                time.sleep(1)
                game()

            if prost2.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                display.blit(zdj1, (0, 0))
                print_msg("Hope to see you again!",pudrowy,125,200,30)
                pygame.display.update()
                time.sleep(1)
                pygame.quit()


def print_msg(msg,colour,a,b,size):
    font = pygame.font.SysFont("comicsansms", size)
    screen=font.render(msg,True,colour)
    display.blit(screen,[a,b])

def game():
    gameExit = False
    gameOver = False
    head_x = szer / 2 #srodek
    head_y = wys / 2
    mv_size = 10 #size bloczku
    FPS = 15 #frames per sec
    head_x_move = 0 #zmiana węża
    head_y_move = 0
    clock = pygame.time.Clock()
    sn_mv = [] #lista z pozycjami węża
    sn_lenght = 1
    choosen=zdj2
    size_of_pic=40 #rozmiar jabłek
    global direction



    randa = random.randrange(0, szer - mv_size,10)
    randb = random.randrange(0, wys - mv_size,10)


    while not gameExit:

        while gameOver==True:
            display.blit(zdj1, (0, 0))
            print_msg("GAME OVER",pudrowy,20,200,30)
            time.sleep(2)
            pygame.display.update()
            display.blit(zdj1, (0, 0))
            print_msg("Press Q to quit or P to stay",pudrowy,72,200,30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        display.blit(zdj1, (0, 0))
                        print_msg("See you soon!",pudrowy,185,200,30)
                        pygame.display.update()
                        time.sleep(2)
                        gameExit=True
                        gameOver=False

                    if event.key==pygame.K_p:
                        game()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and direction!="right":
                    head_x_move = -mv_size
                    head_y_move=0
                    direction="left"

                if event.key==pygame.K_RIGHT and direction!="left":
                    head_x_move= mv_size
                    head_y_move=0
                    direction="right"

                if event.key==pygame.K_DOWN and direction!="up":
                    head_y_move= mv_size
                    head_x_move=0
                    direction="down"

                if event.key==pygame.K_UP and direction!="down":
                    head_y_move= -mv_size
                    head_x_move=0
                    direction="up"

                if event.key==pygame.K_SPACE:
                    pause()


        head_x += head_x_move
        if head_x < 0:
            head_x = szer
        if head_x > szer:
            head_x = 0

        head_y += head_y_move
        if head_y < 0:
            head_y = wys
        if head_y > wys:
            head_y=0

        if head_x>=randa and head_x<=randa+size_of_pic:
            if head_y>=randb and head_y<=randb+size_of_pic:
                randa=random.randrange(0,szer-size_of_pic-20,10)
                randb=random.randrange(0,wys-size_of_pic-20,10)
                sn_lenght += 1

                if sn_lenght%4==1:
                    display.blit(zdj2,(randa,randb))
                    pygame.display.update()
                    choosen=zdj2
                    FPS+=2

                if sn_lenght%4==2:
                    display.blit(zdj3, (randa, randb))
                    pygame.display.update()
                    choosen=zdj3
                    FPS += 2

                if sn_lenght%4==3:
                    display.blit(zdj4, (randa, randb))
                    pygame.display.update()
                    choosen=zdj4
                    FPS += 2

                if sn_lenght%4==0:
                    display.blit(zdj5, (randa, randb))
                    pygame.display.update()
                    choosen=zdj5
                    FPS += 2


        #wlasciwa gra
        display.blit(zdj1, (0,0))
        display.blit(choosen, (randa, randb)) #jabluuszko

        sn_head=[]
        sn_head.append(head_x)
        sn_head.append(head_y)
        sn_mv.append(sn_head)

        if len(sn_mv)>sn_lenght:
            del sn_mv[0]


        for each in sn_mv[:-1]:
            if sn_head==each:
                display.blit(zdj1, (0, 0))
                print_msg("CRAASH",pudrowy,200,200,30)
                pygame.display.update()
                time.sleep(1)
                gameOver=True


        snake(sn_mv)
        pygame.display.update()

        clock.tick(FPS)

    #końcóweczka
    pygame.display.update()
    pygame.quit()
    quit()

menu()
# time.sleep(10)
# game()