import pygame
import random
RED =       (255,   0,   0)
ORANGE =    (0xFF, 0x7F, 0)
YELLOW =    (0xFF, 0x7F, 0)
GREEN =     (  0, 255,   0)
BLUE =      (  0,   0, 255)
D_BLUE =      (  75,   0, 130)
PURPLE =      (  148,   0, 210)
WHITE =     (255, 255, 255)
mycolors= [ RED ,
ORANGE ,
YELLOW ,
GREEN ,
BLUE ,
D_BLUE ,
PURPLE ]




GRAY =      (0xb3,0xb3,0xb3)
WHITE=      (0xFF,0xFF,0xFF)

TEXTCOLOR = (  0,   0,  0)
(width, height) = (800, 600)

running = True
def draw_circle(x,y,color,hide):
    if hide:
        pygame.draw.circle(screen, GRAY, (125+50*x,125+50*y), 21)

    else:
        pygame.draw.circle(screen, TEXTCOLOR, (125+50*x,125+50*y), 21)
        pygame.draw.circle(screen, color,    (125+50*x,125+50*y), 20)
pole=[
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1]
]
# def test_pole():
#     x=0
#     y=0
#     c=pole[y][x]
#     x=x+1
#     c1=pole[y][x]
#     while c==c1:
#     # if c==c1:



def main():
    global running, screen

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TUFF")
    screen.fill(TEXTCOLOR)
    pygame.draw.rect(screen, GRAY,  (100, 100, 450, 450))
    for x in range(9):
        # for y in range(9):
            # c=random.randint(0,6)
            # draw_circle(x,y,mycolors[c],False)
        pygame.draw.line(screen, TEXTCOLOR, [100, 100+50*x], [550, 100+50*x], 1)
        pygame.draw.line(screen, WHITE, [100+1, 100+50*x+1], [550, 100+50*x+1], 1)
        pygame.draw.line(screen, TEXTCOLOR, [ 100+50*x,100], [ 100+50*x,550], 1)
        pygame.draw.line(screen, WHITE, [ 100+50*x+1,100+1], [ 100+50*x+1,550], 1)
    i=0
    while i<5:
        x=random.randint(0,8)
        y=random.randint(0,8)
        c=random.randint(0,6)
        pole[y][x]=c
        i=i+1
        draw_circle(x,y,mycolors[c],False)



    pygame.display.update()
    selected=False
    selected_coord=(0,0)
    selected_color=-1

    while running:
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                #drawCircle()
                pos=getPos()
                x,y=get_coord(pos)

                xs=selected_coord[0]
                ys=selected_coord[1]
                print ('x=',x,'y=',y,selected,selected_color,xs,ys)
                nx=0
                ny=0
                if selected:
                    if x>=0 and x<=8:
                        if y>=0 and y<=8:
                                p_selected_color=pole[y][x]


                                if p_selected_color<0:
                                    #hide old
                                    pole[ys][xs]=-1
                                    draw_circle(xs,ys,GRAY,True)
                                    #show new
                                    pole[y][x]=selected_color
                                    draw_circle(x,y,mycolors[ selected_color],False)
                                    selected=False
                                    i=0
                                    while i<3:
                                        new_color=1
                                        while new_color>=0:
                                            nx=random.randint(0,8)
                                            ny=random.randint(0,8)
                                            c=random.randint(0,6)
                                            new_color=pole[ny][nx]

                                        pole[ny][nx]=c
                                        i=i+1
                                        draw_circle(nx,ny,mycolors[c],False)
                                    pygame.display.update()

                else:

                    if x>=0 and x<=8:
                        if y>=0 and y<=8:
                            selected_coord=(x,y)
                            selected_color=pole[y][x]
                            if selected_color>=0:
                                selected=True




                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False
def get_coord(pos):
    xe=pos[0]
    ye=pos[1]
    x=int((xe-100)/50 )
    y=int((ye-100)/50 )
    return x,y

def getPos():
    pos = pygame.mouse.get_pos()
    x,y=get_coord(pos)
    print (x,y)
    return (pos)



if __name__ == '__main__':
    main()
