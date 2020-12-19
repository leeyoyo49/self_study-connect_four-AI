import sys
import pygame
from pygame.locals import QUIT
GRAVITY = .02
class Board():
    def __init__(self):
        self.board_list = [[0 for x in range(7)] for x in range(6) ]
        self.row = 6
        self.column = 7
    def grid_drop(coordinate):
        pass

class Coordinate(pygame.sprite.Sprite):
    
    def __init__(self,pos,screen,guy):
        super().__init__()
        print("create")
        self.pos = pos
        self.screen = screen
        self.image = guy
        self.rect = self.image.get_rect(center=pos)
        self.speed_y = 0
        self.position_y = pos[1]
    
    def update(self):
        self.speed_y += GRAVITY
        self.position_y += self.speed_y
        self.rect.y = self.position_y

# 初始化
TURN = 1
pygame.init()
Board = Board()
# 建立 window 視窗畫布，大小為 700x700
window_surface = pygame.display.set_mode((700, 700))
# 設置視窗標題為 connect four
pygame.display.set_caption('Connect four !!')
# 清除畫面並填滿背景色 https://microdnd.pixnet.net/blog/post/103334755
window_surface.fill((220, 220 ,220))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
board_pic = pygame.image.load("pics/board.PNG")
trump = pygame.image.load("pics/trump.PNG")
biden = pygame.image.load("pics/biden.PNG")
#smoothscale 調整大小、 conver_alpha 讓ＰＮＧ的空白存在
board_pic = pygame.transform.smoothscale(board_pic,(700,700)).convert_alpha()
trump = pygame.transform.smoothscale(trump,(90,90)).convert_alpha()
biden = pygame.transform.smoothscale(biden,(90,90)).convert_alpha()
# window_surface.blit(trump,(14,124)) #左上角的位置

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()
coordinates = pygame.sprite.Group()

# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:

#回傳x在哪一塊 然後叫coordinate函式 還有board要處理那個column有多少coordinate 並且扔給coordinate
            pos = pygame.mouse.get_pos()
            x_part = pos[0] // 100
            #圖有點歪...
            if 3<=x_part<= 5:
                x_part -= 0.07
            #choose which pic 1 ->trump, 0->biden
            if TURN:
                coordinates.add(Coordinate((x_part*100+50,122),window_surface,trump))
                TURN = 0
            else:
                coordinates.add(Coordinate((x_part*100+50,122),window_surface,biden))
                TURN = 1 
        elif event.type == QUIT:
            # 當使用者結束視窗，程式也結束
            pygame.quit()
            sys.exit()
    #讓coordinate＆background更新
    coordinates.update()

    window_surface.fill((220,220,220))
    coordinates.draw(window_surface)

    window_surface.blit(board_pic,(0,0))
    pygame.display.flip()
