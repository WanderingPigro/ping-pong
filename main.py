from pygame import *

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

player1 = GameSprite('racket.png', 30,200,50,150,4)
player2 = GameSprite('racket.png', 520, 200,50,150,4)


while gameover == False:
    for e in event.get():
        if e.type == QUIT:
            gameover == True

    window.fill(bgcolor)
    player1.draw()
    player2.draw()
    display.update()
    clock.tick(60)