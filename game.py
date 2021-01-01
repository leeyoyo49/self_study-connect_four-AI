import sys
import pygame
from pygame.locals import QUIT
GRAVITY = .05

class Board():
    def __init__(self):
        # 初始化
        self.TURN = 1
        pygame.init()
        # 建立 window 視窗畫布，大小為 700x700
        self.window_surface = pygame.display.set_mode((700, 700))
        # 設置視窗標題為 connect four
        pygame.display.set_caption('Connect four !!')
        # 清除畫面並填滿背景色 https://microdnd.pixnet.net/blog/post/103334755
        self.window_surface.fill((220, 220 ,220))
        # blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
        self.board_pic = pygame.image.load("pics/board.PNG")
        self.trump = pygame.image.load("pics/trump.PNG")
        self.biden = pygame.image.load("pics/biden.PNG")
        #smoothscale 調整大小、 conver_alpha 讓ＰＮＧ的空白存在
        self.board_pic = pygame.transform.smoothscale(self.board_pic,(700,700)).convert_alpha()
        self.trump = pygame.transform.smoothscale(self.trump,(90,90)).convert_alpha()
        self.biden = pygame.transform.smoothscale(self.biden,(90,90)).convert_alpha()
        # window_surface.blit(trump,(14,124)) #左上角的位置

        # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
        pygame.display.update()
        self.coordinates = pygame.sprite.Group()
        self.board_list = [0 for x in range(42) ]
        self.row = [0 for x in range(6)]
        self.column = [0 for x in range(7)] #一行幾個

    def game(self):
        # 事件迴圈監聽事件，進行事件處理
        while True:
            # 迭代整個事件迴圈，若有符合事件則對應處理
            for event in pygame.event.get():
                # print(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONUP:

        #回傳x在哪一塊 然後叫coordinate函式 還有board要處理那個column有多少coordinate 並且扔給coordinate
                    pos = pygame.mouse.get_pos()
                    x_part = pos[0] // 100
                    how_many_coord_under = self.column[x_part]
                    self.column[x_part] += 1
                    whose_coord = 7*(5-how_many_coord_under)+x_part
                    #圖有點歪...
                    if 2<=x_part<= 5:
                        x_part -= 0.07
                    #choose which pic 1 ->trump, 0->biden
                    if how_many_coord_under>5:
                        continue
                    if self.TURN:
                        self.coordinates.add(self.Coordinate((x_part*100+50,122),self.window_surface,self.trump,x_part,how_many_coord_under))
                        self.board_list[whose_coord] = 1 
                        self.TURN = 0
                        a = 200
                        while a:
                            #讓coordinate＆background更新
                            self.coordinates.update()

                            self.window_surface.fill((220,220,220))
                            self.coordinates.draw(self.window_surface)

                            self.window_surface.blit(self.board_pic,(0,0))
                            pygame.display.flip()
                            a-=1
                    else:
                        self.coordinates.add(self.Coordinate((x_part*100+50,122),self.window_surface,self.biden,x_part,how_many_coord_under))                    
                        self.board_list[whose_coord] = 2
                        self.TURN = 1 
                        a = 200
                        while a:
                            #讓coordinate＆background更新
                            self.coordinates.update()

                            self.window_surface.fill((220,220,220))
                            self.coordinates.draw(self.window_surface)

                            self.window_surface.blit(self.board_pic,(0,0))
                            pygame.display.flip()
                            a -=1
                if self.win():
                    pygame.quit()
                elif event.type == QUIT:
                    # 當使用者結束視窗，程式也結束
                    pygame.quit()
                    sys.exit()
                self.window_surface.fill((220,220,220))
                self.coordinates.draw(self.window_surface)

                self.window_surface.blit(self.board_pic,(0,0))
                pygame.display.flip()
    def win(self):
        for x in range(7,43,7):
            temp = self.board_list[x-7:x]
            if temp[3]:
                for y in range(4):
                    if temp[y] == temp[y+1] == temp[y+2] == temp[y+3]:
                        return 1
                        pass
        for x in range(0,7):
            temp = [self.board_list[x]]
            for y in range(7,36,7):
                temp.append(self.board_list[x+y])
            if temp[3]:
                for z in range(3):
                    if temp[z] == temp[z+1] == temp[z+2] == temp[z+3]:
                        return 1
        for x in range(3,7):
            for y in range(3):
                loc = x + y*7
                if self.board_list[loc]:
                    if self.board_list[loc] == self.board_list[loc+6] == self.board_list[loc+12] == self.board_list[loc+18]:
                        return 1
        for x in range(0,4):
            for y in range(3):
                loc = x + y*7
                if self.board_list[loc]:
                    if self.board_list[loc] == self.board_list[loc+8] == self.board_list[loc+16] == self.board_list[loc+24]:
                        #win 往右下噴
                        return 1
        return 0
    class Coordinate(pygame.sprite.Sprite):
        
        def __init__(self,pos,screen,guy,which_column,coords_under):
            super().__init__()
            self.column = which_column
            self.coords_under = coords_under
            self.pos = pos
            self.screen = screen
            self.image = guy
            self.rect = self.image.get_rect(center=pos)
            self.speed_y = 0
            self.position_y = pos[1]
        
        def update(self):
            self.speed_y += GRAVITY
            self.position_y += self.speed_y
            if self.position_y < (615 - (self.coords_under)*100):
                self.rect.y = self.position_y
            else: 
                if self.coords_under > 2:
                    self.rect.y = 621 - self.coords_under*100
                else:
                    self.rect.y = 611 - self.coords_under*100

while 1:
    bd = Board()
    bd.game()