import pygame
from settings import *
import random

def draw_background():
    screen.fill(BACKGROUND_COLOR)

def gen_buttons():
    x,y,w,h=640,20,100,30
    buttons=[]
    for i in range (1,4):
        buttons.append({'name': 'Level '+str(i), 'coordinates': (x,y,w,h)})
        y=y+h+10
    buttons.append({'name': 'Play', 'coordinates': (x,y,w,h)})

    return(buttons)

def draw_buttons():
    for b in buttons[:len(buttons)]:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+17,b['coordinates'][1]+3))
    
    if selected!=-1:
        pygame.draw.rect(screen, PINK, buttons[selected]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons[selected]['coordinates'], 3)
        text=font.render(buttons[selected]['name'], True, BLACK)
        screen.blit(text, (buttons[selected]['coordinates'][0]+17,buttons[selected]['coordinates'][1]+3))

    pygame.draw.rect(screen, GRAY, buttons[-1]['coordinates'])
    pygame.draw.rect(screen, BLACK,  buttons[-1]['coordinates'], 3)
    text=font.render( buttons[-1]['name'], True, BLACK)
    screen.blit(text, ( buttons[-1]['coordinates'][0]+30, buttons[-1]['coordinates'][1]+3))

def draw_color_bar():
    colors=[]
    w=70
    x_offset=90
    y_offset=50
    x,y=x_offset,SCREEN_HEIGHT-y_offset-w
    for i in COLORS:
        colors.append([x,y,w,w])
        pygame.draw.rect(screen, i, (x,y,w,w), border_radius=10)
        pygame.draw.rect(screen, WHITE, (x,y,w,w), 3, 10)
        x=x+w-2

def draw_squares(n_per_row=3):
    matrix=[]

    if(n_per_row/(70*6)<(SCREEN_HEIGHT-170)/5):
        w=(SCREEN_HEIGHT-170)/5
    else:
        w=(70*6)/n_per_row
    print(w)
    x_offset=(560-90)/4/(n_per_row-1)
    x_offset=-2
    y_offset=-2
    x,y=90+(70*6-w*n_per_row)/2,30
    for row in range(5):
        temp=[]
        x=90+(70*6-w*n_per_row)/2
        for col in range(n_per_row):
            pygame.draw.rect(screen, WHITE, (x,y,w,w), 3, 10)
            temp.append([x,y,w,w])
            x=x+w+x_offset
        matrix.append(temp)
        y=y+w+y_offset
        return(matrix)

def gen_puzzle(n_per_row=3):
    puzzle=[]
    for i in range(n_per_row):
        puzzle.append(random.choice(COLORS))
    return(puzzle)






if __name__=='__main__':
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Campo minato♥')
    font = pygame.font.SysFont('arial', 20)

    win=False
    loose=False
    selected=-1
    game_started=False
    buttons=gen_buttons()
    draw_buttons()
    draw_color_bar()
    matrix=draw_squares()

    run  = True
    number=0

    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()

                for i in range (len(buttons)):
                    if(x>=buttons[i]['coordinates'][0] and x<=buttons[i]['coordinates'][0]+buttons[i]['coordinates'][2] and y>=buttons[i]['coordinates'][1] and y<=buttons[i]['coordinates'][1]+buttons[i]['coordinates'][3]):
                        if(i<len(buttons)-1):
                            selected=i
                            if(not(game_started)):
                                select_game=selected
                            draw_buttons()
                            break
                        elif(i==4):
                            if(selected!=-1):
                                pygame.draw.rect(screen, BACKGROUND_COLOR, (640,490,100,100))
                                select_game=selected
                                selected=-1
                                win=False
                                loose=False
                                game_started=True
                                first_cell=True
                                buttons=gen_buttons()
                                draw_buttons()
                            break
                else:
                    selected=-1
                draw_buttons()


                    

            if (event.type == pygame.KEYDOWN):
                pass


        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()