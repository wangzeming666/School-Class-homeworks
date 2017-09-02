import pygame, random, sys

class Game2048(pygame.sprite.Sprite):
    #游戏初始化
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #绘制矩形


        # 设置字体、大小
        
        # 是否加粗，是
        number.set_bold(True)
        # 设置文字内容， 颜色
        num = number.render("asdfasdfasd", True, (0,0,0))
        #绘制文字
        num.blit(num,(20,20)) 

















# Pygame初始化
pygame.init()

screencaption=pygame.display.set_caption('Game2048')
screen = pygame.display.set_mode([620,620])
number = pygame.font.SysFont('arial', 12)
screen.fill([255,255,255])
G = Game2048()
clock = pygame.time.Clock()


while True:
    clock.tick(30)
    # 检测事件
    for event in pygame.event.get():




        # 设置叉号检测退出
        if event.type==pygame.QUIT:
            sys.exit()

    #刷新画面
    pygame.display.update()
