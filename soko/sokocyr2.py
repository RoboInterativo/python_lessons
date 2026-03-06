from pygamecyr import *








class МояИгра(Игра):

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
                    pass

                if столбец==3:
                    pass
                if столбец==2:
                    pass
                if столбец==0:
                    координаты_фона.top=y_coord
                    координаты_фона.left=x_coord
                    self.экран.blit(фон, координаты_фона)

    def перед_игрой(self):
        pass




    def игровой_цикл(self):
        pass


    def столкновения(self):
        pass








игра=МояИгра()
игра.запуск()
