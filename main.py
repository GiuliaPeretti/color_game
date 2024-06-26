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
    return colors

def draw_squares():
    matrix=[]
    matrix_status=[]
    
    if(n_per_row/(70*6)<(SCREEN_HEIGHT-170)/5):
        w=(SCREEN_HEIGHT-170)/5
    else:
        w=(70*6)/n_per_row
    x_offset=-2
    y_offset=-2
    x,y=90+(70*6-w*n_per_row)/2,30
    for row in range(4):
        temp1=[]
        temp2=[]
        x=90+(70*6-w*n_per_row)/2
        for col in range(n_per_row):
            pygame.draw.rect(screen, WHITE, (x,y,w,w), 3, 10)
            temp1.append([x,y,w,w])
            temp2.append(-1)
            x=x+w+x_offset
        matrix.append(temp1)
        matrix_status.append(temp2)
        y=y+w+y_offset

    y=y+15
    x=90+(70*6-w*n_per_row)/2
    temp1=[]
    for col in range(n_per_row):
        pygame.draw.rect(screen, WHITE, (x,y,w,w), 3, 10)
        temp1.append([x,y,w,w])
        x=x+w+x_offset
    matrix.append(temp1)
    return(matrix, matrix_status)

def gen_puzzle():
    puzzle=[]
    for i in range(n_per_row):
        puzzle.append(random.randint(0,len(COLORS)-1))
    return(puzzle)

def show_solution():
    print("puzzle: "+ str(puzzle))
    for i in range(len(puzzle)):
        pygame.draw.rect(screen, COLORS[puzzle[i]], matrix[4][i], border_radius=10)
    _=draw_squares()

def color_square(i):
    # for row in range(len(matrix_status)):
    row=current_row
    for col in range(len(matrix[row])):
        if matrix_status[row][col]==-1:
            matrix_status[row][col]=i
            pygame.draw.rect(screen, COLORS[i], matrix[row][col], border_radius=10)
            break

    _,_=draw_squares()


def check_win(row):
    print("check_win")
    win=True
    lost=False
    print(matrix_status[row])
    print(puzzle)
    for i in range (len(matrix_status[row])):
        if matrix_status[row][i]!=puzzle[i]:
            win=False
    if(not(win) and row==3):
        lost=True
    end(win,lost)

def end(win, lost):
    font = pygame.font.SysFont('arial', 40)

    print("check_win")
    print(win,lost)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (600,400, 200,100))
    if(win):
        text="WIN"
        text=font.render( text, True, RED)
        screen.blit(text, (650,450))
    elif(lost):
        text="LOST"
        text=font.render( text, True, RED)
        screen.blit(text, (650,450))
        show_solution()
    
def draw_minimap():
    pygame.draw.rect(screen, BACKGROUND_COLOR, (630,240,200,200))
    w=100/n_per_row
    y=250
    for row in range (4):
        x=640
        for col in range(n_per_row):
            if (matrix_status[row][col]==puzzle[col]):
                color=GREEN
            elif(matrix_status[row][col] in puzzle):
                color=YELLOW
            elif(matrix_status[row][col]==-1):
                color=BACKGROUND_COLOR
            else:
                color=RED
            pygame.draw.rect(screen, color, (x,y,w,w), border_radius=10)
            pygame.draw.rect(screen, WHITE, (x,y,w,w), 3, 10)
            x=x+w
        y=y+w

def delete_color():
    for col in range(n_per_row-1,-1, -1):
        
        if matrix_status[current_row][col]!=-1:
            pygame.draw.rect(screen, BACKGROUND_COLOR, matrix[current_row][col], border_radius=10)
            matrix_status[current_row][col]=-1
            break
    _,_=draw_squares()
            






if __name__=='__main__':
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Campo minato♥')
    font = pygame.font.SysFont('arial', 20)

    win=False
    lost=False
    selected=-1
    game_started=False
    n_per_row=3
    current_row=0
    buttons=gen_buttons()
    draw_buttons()
    print(buttons)
    colors=draw_color_bar()

    run  = True
    number=0

    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                print(x,y)

                for i in range (len(colors)):
                    if (x>=colors[i][0] and x<=colors[i][0]+colors[i][2] and y>=colors[i][1] and y<=colors[i][1]+colors[i][3]):
                        color_square(i)


                for i in range (len(buttons)):
                    if(x>=buttons[i]['coordinates'][0] and x<=buttons[i]['coordinates'][0]+buttons[i]['coordinates'][2] and y>=buttons[i]['coordinates'][1] and y<=buttons[i]['coordinates'][1]+buttons[i]['coordinates'][3]):
                        print(i)
                        if(i<len(buttons)-1):
                            selected=i
                            if(not(game_started)):
                                select_game=selected
                            draw_buttons()
                            break
                        elif(i==3):
                            print("play")
                            if(selected!=-1):
                                pygame.draw.rect(screen, BACKGROUND_COLOR, (600,400, 200,100))
                                pygame.draw.rect(screen, BACKGROUND_COLOR, (0,0,520,470))
                                pygame.draw.rect(screen, BACKGROUND_COLOR, (640,490,100,100))
                                select_game=selected
                                n_per_row=select_game+3
                                selected=-1
                                win=False
                                loose=False
                                game_started=True
                                first_cell=True
                                draw_buttons()
                                matrix, matrix_status=draw_squares()
                                puzzle=gen_puzzle()
                                draw_minimap()

                            break
                else:
                    selected=-1
                draw_buttons()
            
                


                    

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    print("return")
                    if (-1 not in matrix_status[current_row]):
                        check_win(current_row)
                        current_row+=1
                        draw_minimap()
                elif(event.key==pygame.K_BACKSPACE):
                    delete_color()


        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()