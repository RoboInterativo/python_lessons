from pygamecyr import *
class МояИгра(Игра):
    def перед_игрой(self):
        self.x=1
        self.y=1
        self.dx=5
        self.dy=5
    def игровой_цикл(self):
        self.заливка(ЧЕРНЫЙ)


        прямоугольник(self.экран, БЕЛЫЙ, (self.x, self.y, 10, 10))
        self.x=self.x+self.dx
        self.y=self.y+self.dy

    def столкновения(self):
        if (self.x+self.dx >= self.ШИРИНА ):
            self.dx=-self.dx

        if (self.y+self.dy>=self.ВЫСОТА):
            self.dy=-self.dy

        if (self.x+self.dx<=0):
            self.dx=-self.dx

        if (self.y+self.dy<=0):
            self.dy=-self.dy




игра=МояИгра()
игра.запуск()
