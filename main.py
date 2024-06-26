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
        x=x+w+10

def draw_squares(n_per_row=3):

    w=3*(560-90)/4
    x_offset=90
    y_offset=50
    x,y=x_offset,SCREEN_HEIGHT-y_offset-w
    for row in range(5):
        x=x_offset,SCREEN_HEIGHT-y_offset-w
        for col in range(n_per_row):
            pygame.draw.rect(screen, WHITE, (100,100,50,50), 3, 10)
            x=x+w+10






if __name__=='__main__':
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Campo minato♥')
    font = pygame.font.SysFont('arial', 20)

    selected=-1
    buttons=gen_buttons()
    draw_buttons()
    draw_color_bar()

    run  = True
    number=0

    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                    

            if (event.type == pygame.KEYDOWN):
                pass


        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()