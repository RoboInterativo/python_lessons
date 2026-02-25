from pygamecyr import *

стена, координаты_стены=загрузить_картинку("img/wall.png")
фон, координаты_фона= загрузить_картинку("img/empty.png")
изображение_ящика, координаты_ящика= загрузить_картинку("img/box.png")
цель, координаты_цели= загрузить_картинку("img/place.png")
изображение_чела, координаты_чела= загрузить_картинку("img/man.png")
вверх,вправо,вниз,влево=range(4)

class Ящик:
    def __init__(self,x,y):
        # super(, self).__init__()
        self.изображение_ящика=изображение_ящика
        self.координаты_ящика=координаты_ящика
        #self.boxrect =
        self.x=  x
        self.y = y
    def рисовать(self,экран):
        x_coord=26*(self.x-1)
        y_coord=26*(self.y-1)

        self.координаты_ящика.left=x_coord
        self.координаты_ящика.top=y_coord
        экран.blit(self.изображение_ящика, self.координаты_ящика)
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

class Чел:

    def __init__(self,x,y):
        # super(, self).__init__()
        self.изображение_чела=изображение_чела
        self.координаты_чела = координаты_чела
        self.x=  x
        self.y = y

    def рисовать(self,экран):
        x_coord=26*(self.x-1)
        y_coord=26*(self.y-1)
        self.координаты_чела.left=x_coord
        self.координаты_чела.top=y_coord
        экран.blit(self.изображение_чела, self.координаты_чела)

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


    def движение(self,направление):
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



class МояИгра(Игра):
    def рисуем_карту(self):
        x=0
        y=0
        for строка in self.карта:

            x=0
            y +=1
            for столбец in строка:
                x +=1

                x_coord=26*(x-1)
                y_coord=26*(y-1)
                #print (x_coord,y_coord,col)
                if столбец==4:
                    координаты_стены.top=y_coord
                    координаты_стены.left=x_coord
                    self.экран.blit(стена, координаты_стены)
                if столбец==1:
                    # координаты_ящика.top=y_coord
                    # координаты_ящика.left=x_coord
                    ящик=Ящик(x,y)
                    ящик.рисовать(self.экран)
                    self.ящики.append(ящик)
                    #self.ящики.append( (x_coord,y_coord))
                    #self.экран.blit(ящик, координаты_ящика)
                if столбец==3:
                    координаты_цели.top=y_coord
                    координаты_цели.left=x_coord
                    # ящик=
                    # self.экран.blit(цель, координаты_цели)
                if столбец==2:
                    self.чел=Чел(x,y)
                    self.чел.рисовать(self.экран)

                    # координаты_чела.top=y_coord
                    # координаты_чела.left=x_coord
                    # self.экран.blit(чел, координаты_чела)
                if столбец==0:
                    координаты_фона.top=y_coord
                    координаты_фона.left=x_coord
                    self.экран.blit(фон, координаты_фона)
#===================================================================
    def клавиши(self):
        if event.key == КЛАВИША_ВЛЕВО:
            pygame.display.flip()
        if event.key == КЛАВИША_ВПРАВО:
            pygame.display.flip()
        if event.key == КЛАВИША_ВНИЗ:
            pygame.display.flip()
        if event.key == КЛАВИША_ВВЕРХ:
            pygame.display.flip()

    def перед_игрой(self):
        self.карта=загрузить_карту("first.map")
        self.заливка(ЧЕРНЫЙ)
        self.ящики=[]
        self.чел=None
        #self.экран.blit(стена, координаты_стены)
        self.рисуем_карту()





    def игровой_цикл(self):
        pass





    def столкновения(self):
        pass








игра=МояИгра()
игра.запуск()
