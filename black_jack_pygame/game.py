import pygame
import pygame.gfxdraw
import random
import time

ranks=['A','2', '3', '4','5', '6', '7', '8', '9','T', 'J', 'Q', 'K' ]
suits=[ '♥','♦','♣','♠']
screen = pygame.display.set_mode((800, 600))
pygame.init()
size_x=70
size_y=105
delta=5
#55aa55
BGCOLOR=(0x55,0xAA,0x55)
screen.fill(BGCOLOR)


desk_image = pygame.image.load('desk2.png')
desk_image.convert()
stop_image = pygame.image.load('stop.png')
stop_image.convert()

def make_desk():
    desk=[]
    for r in ranks:
        for m in suits:
            card=str(r)+str(m)
            desk.append(card)
    return (desk)


def count_score(hand):
    score=0
    for card in hand:

        if card[0] in      ['J', 'Q', 'K','T']:
            score=score+10
        elif card[0]=='A':
            score=score+11
        else:
            score=score+eval(card[0])

    return score

def get_card_image(desk_image,card):
    if card=="FACE1":
        x=13
        y=0
    else:
        rank=card[0]
        suit=card[1]
        x=ranks.index(rank)
        y=suits.index(suit)
    cropped = pygame.Surface((size_x, size_y))
    #card_rect=((5+size_x)*x, (4+size_y)*y, 5+size_x+(size_x+5)*x , 5+size_y+(4+size_y)*y)
    sizeb_x=75
    sizeb_y=109
    xe1=x*sizeb_x+5
    ye1=y*sizeb_y+5
    xe2=xe1+size_x
    ye2=ye1+size_y
    card_rect=(xe1,ye1,xe2,ye2)


    x1=5
    print(card_rect)
    cropped.blit(desk_image, (0, 0), card_rect)
    print (x,y)
    return cropped
def show_desk():
    for x in range (10):
        card_image=get_card_image(desk_image,'FACE1')

        screen.blit(card_image,(500+(1.5)*x,100+(2)*x))
        pygame.display.update()
def show_hand(hand,is_crupe,show_card):
    surf1 = pygame.Surface((200, 200))
    surf1.fill(BGCOLOR)
    rect = pygame.Rect((20, 400, 120, 420))
    screen.blit(surf1, rect)
    if is_crupe:
        top=50
        x=0

        for card in hand:
            if show_card:
                card_image=get_card_image(desk_image,card)
            else:
                if hand.index(card)==0:
                    card_image=get_card_image(desk_image,card)
                else:

                    card_image=get_card_image(desk_image,'FACE1')
            screen.blit(card_image,(100+(size_x+10)*x,top))
            pygame.display.update()
            x=x+1
    else:
        top=450
        x=0
        font = pygame.font.SysFont(None, 24)
        img = font.render('Крупье', True, (0,0,0))
        screen.blit(img, (20, 20))
        font = pygame.font.SysFont(None, 24)
        img = font.render('Игрок: ({})'.format(count_score (hand)), True, (0,0,0))
        screen.blit(img, (20, 400))
        for card in hand:
            card_image=get_card_image(desk_image,card)
            screen.blit(card_image,(100+(size_x+10)*x,top))
            pygame.display.update()
            x=x+1
#card='K♠'
card='J♣'
card='3♦'
card='FACE1'

running = True

def start_game():
    global desk
    global crupe
    global hand
    desk=make_desk()
    print("Крупье мешает колоду")
    random.shuffle(desk)
    print("Сдает по 2 карты, себе и вам")
    crupe=[]
    hand=[]
    crupe.append(desk.pop())
    hand.append(desk.pop())
    crupe.append(desk.pop())

    hand.append(desk.pop())

    # card_image=get_card_image (desk_image,'T♣')
    # screen.blit(card_image,(110,50) )
    pygame.display.update()

    show_hand(crupe,True,False)
    show_hand(hand,False,False)
    show_desk()

    screen.blit(stop_image,(500,400))
    pygame.display.update()
start_game()
game_over=False
while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            sp = event.pos
            print(sp)
            x=sp[0]
            y=sp[1]
# (684, 582)
# (515, 419)
            if x>515 and x<684:
                if y> 419 and y<582:
                    print('STAY')
                    if game_over:
                        pass
                    else:
                        show_hand(crupe,True,True)
                        show_hand(hand,False,True)
                        pygame.display.update()
                        game_over=True


            if x>506 and x<579:
                if y> 104 and y<218:
                    if game_over:
                        #time.sleep(5) #
                        screen.fill(BGCOLOR)

                        pygame.display.update()
                        game_over=False
                        start_game()

                    else:
                        hand.append(desk.pop())
                        show_hand(hand,False,False)

                        if count_score (crupe)<=10:
                            print('Карты крупье думает и берет еще карту')
                            crupe.append(desk.pop())
                            show_hand(crupe,True,False)
                        pygame.display.update()
                        if count_score (crupe)>=21:
                             font = pygame.font.SysFont(None, 24)
                             img = font.render('Перебор, начать заново? Кликни по колоде.', True, (0,0,0))
                             screen.blit(img, (420, 20))
                             show_hand(crupe,True,True)
                             show_hand(hand,False,True)
                             pygame.display.update()

                        if count_score (hand)>=21:
                             font = pygame.font.SysFont(None, 24)
                             img = font.render('Перебор, начать заново? Кликни по колоде.', True, (0,0,0))
                             screen.blit(img, (420, 20))
                             show_hand(crupe,True,True)
                             show_hand(hand,False,True)
                             pygame.display.update()



                             game_over=True
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
