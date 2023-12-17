from pygame import *
import time as t
w = 600
h = 500

window = display.set_mode((w, h))
bgcolor = (75, 60, 240)

clock = time.Clock()

gameover = False

class GameSprite(sprite.Sprite):
    def __init__(self, img,x,y,w,h,s):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.speed = s
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keypressed = key.get_pressed()

        if keypressed[K_w] == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if keypressed [K_s] == True and self.rect.bottom < h:
            self.rect.y += self.speed
    def update2(self):
        keypressed = key.get_pressed()

        if keypressed[K_UP] == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if keypressed [K_DOWN] == True and self.rect.bottom < h:
            self.rect.y += self.speed

player1 = Player('racket.png', 0,200,50,150,4)
player2 = Player('racket.png', 550, 200,50,150,4)

playergroup = sprite.Group()
playergroup.add(player1)
playergroup.add(player2)

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, s):
        super().__init__(img, x, y, w, h, s)
        self.speed_x = self.speed
        self.speed_y = self.speed
        self.bounce_cd = False
        self.bounce_cdstart = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.bottom >= h:
            self.speed_y *= -1
        if self.bounce_cd == False:
            if len(sprite.spritecollide(self, playergroup, False)) != 0:
                self.speed_x *= -1
                self.bounce_cd = True
                self.bounce_cdstart = t.time()
        if self.bounce_cd == True:
            if t.time() - self.bounce_cdstart >= 0.5:
                self.bounce_cd = False

ball = Ball('tensis_ball.png', 200, 200,50,50,4) 


while gameover == False:
    for e in event.get():
        if e.type == QUIT:
            gameover = True

    window.fill(bgcolor)
    playergroup.draw(window)

    player1.draw()
    player2.draw()
    ball.draw()
    
    ball.update()
    player1.update1()
    player2.update2()
    display.update()
    clock.tick(60)