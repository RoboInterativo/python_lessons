import sys, pygame
# import csv

with open('first.map') as csvfile:
    mapf = csvfile.readlines()
map=[]
for line in mapf:
    row=line.split(',')
    row_int=[]
    for item in row:
        row_int.append(int(item))
    map.append(row_int)


pygame.init()
#
size = width, height = 640, 480
# # speed = [1, 1]
black = 255, 255, 255

screen = pygame.display.set_mode(size)

screen.fill(black)
wall = pygame.image.load("img/wall.png")
back= pygame.image.load("img/empty.png")
box= pygame.image.load("img/box.png")
place= pygame.image.load("img/place.png")
man= pygame.image.load("img/man.png")
wallrect = wall.get_rect()
backrect = back.get_rect()
boxrect = box.get_rect()
placerect = place.get_rect()
manrect = man.get_rect()

class Box(object):
    def move_left(self):
        # if map[self.y-1][self.x-1-1]==4:
        #     pass
        # else:
        # self.erase_draw()
        self.x=self.x-1
        print(self.x)
        self.draw()

    def move_up(self):
        self.y=self.y-1
        print(self.y)
        self.draw()

    def move_right(self):
        self.x=self.x+1
        print(self.x)
        self.draw()

    def move_down(self):
        self.y=self.y+1
        print(self.y)
        self.draw()

    def draw(self):
        x_coord=26*(self.x-1)
        y_coord=26*(self.y-1)

        self.boxrect.left=x_coord
        self.boxrect.top=y_coord
        screen.blit(self.box, self.boxrect)

    def __init__(self, box,x,y):
        # super(, self).__init__()
        self.box=box
        self.boxrect=box.get_rect()
        #self.boxrect =
        self.x=  x
        self.y = y

class Man(object):
    def erase_draw(self):
        x_coord=26*(self.x-1)
        y_coord=26*(self.y-1)

        if map[self.y-1][self.x-1]==3:
            place= pygame.image.load("img/place.png")
            placerect = place.get_rect()
            placerect.left=x_coord
            placerect.top=y_coord
            screen.blit(place,placerect)
        else:
            back= pygame.image.load("img/empty.png")
            backrect = back.get_rect()
            backrect.left=x_coord
            backrect.top=y_coord
            screen.blit(back,backrect)



    def draw(self):
        x_coord=26*(self.x-1)
        y_coord=26*(self.y-1)
        self.manrect.left=x_coord
        self.manrect.top=y_coord
        screen.blit(self.man, self.manrect)

    def move_left(self):
        allow_move = True
        for item in boxes:
            if item.x==self.x-1:
                if item.y==self.y:
                    for item2 in boxes:
                        if item2.y==item.y:
                            if item.x==item2.x-1:
                                allow_move=False
                    if allow_move:
                        index=boxes.index(item)
                        boxes[index].move_left()

        if map[self.y-1][self.x-1-1] != 4:
            if allow_move:
                self.erase_draw()
                self.x=self.x-1
                print(self.x)
                self.draw()

    def move_right(self):
        if map[self.y-1][self.x-1+1]==4:
            pass
        else:
            self.erase_draw()
            self.x=self.x+1
            print(self.x)
            self.draw()

    def move_up(self):
        allow_move = True
        for item in boxes:
            if item.x==self.x:
                if item.y==self.y-1:
                    for item2 in boxes:
                        if item2.y==item.y-1:
                            if item.x==item2.x:
                                allow_move=False
                    if allow_move:
                        index=boxes.index(item)
                        boxes[index].move_up()

        if map[self.y-1-1][self.x-1]==4:
            pass
        else:
            self.erase_draw()
            self.y=self.y-1
            print(self.y)
            self.draw()

    def move_down(self):
        if map[self.y-1+1][self.x-1]==4:
            pass
        else:
            self.erase_draw()
            self.y=self.y+1
            print(self.y)
            self.draw()

    def __init__(self, man,x,y):
        # super(, self).__init__()
        self.man=man
        self.manrect = man.get_rect()
        self.x=  x
        self.y = y




#
x=0
y=0


boxes=[]
for row in map:

    x=0
    y +=1
    for col in row:
        x +=1

        x_coord=26*(x-1)
        y_coord=26*(y-1)
        print (x_coord,y_coord,col)
        if col==4:
            wallrect.top=y_coord
            wallrect.left=x_coord
            screen.blit(wall, wallrect)
        if col==1:
            box2=Box(box,x,y)
            box2.draw()
            boxes.append(box2)
            # boxrect.top=y_coord
            # boxrect.left=x_coord
            # screen.blit(box, boxrect)
        if col==3:
            placerect.top=y_coord
            placerect.left=x_coord
            screen.blit(place, placerect)
        if col==2:
            man2=Man(man,x,y)
            man2.draw()
            # manrect.top=y_coord
            # manrect.left=x_coord
            # screen.blit(man, manrect)
        if col==0:
            backrect.top=y_coord
            backrect.left=x_coord
            screen.blit(back, backrect)







pygame.display.flip()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                man2.move_up()
                pygame.display.flip()
            if event.key == pygame.K_LEFT:
                man2.move_left()
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                man2.move_right()
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                man2.move_down()
                pygame.display.flip()
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
    #screen.fill(black)

    # screen.blit(wall, wallrect)
    # wallrect.top=56
    # screen.blit(wall, wallrect)
    #pygame.display.flip()
