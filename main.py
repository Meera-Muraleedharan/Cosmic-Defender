import pygame
import math

sw = 800
sh = 800
bg = pygame.image.load('assets/background-black.png')
asteroid = pygame.image.load('assets/asteroid.jpg')
rocket = pygame.image.load('assets/rocket.png')
meteorite = pygame.image.load('assets/meteorite.png')

pygame.display.set_caption('Cosmic defenders')

win = pygame.display.set_mode((sw, sh))
scaled_bg = pygame.transform.scale(bg, (2 * bg.get_width(), 2 * bg.get_height()))

clock = pygame.time.Clock()
gameover = False

class Player(object):
    def __init__(self):
        self.img = rocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sin * self.h//2)
    
    
    
    def draw(self, win):
        # win.blit(self.img, [self.x, self.y, self.w, self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sin * self.h//2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sin * self.h//2)    


    def moveForward(self):
        self.x -= self.cosine * 6
        self.y += self.sin * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sin = -math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sin * self.h//2)    


        

def redrawGameWindow():
    win.blit(scaled_bg, (0,0))
    player.draw(win)
    pygame.display.update()

player = Player()

run = True
# while run:
#     clock.tick(60)
#     if not gameover:
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             player.turnLeft()
#         if keys[pygame.K_RIGHT]:
#             player.turnRight()
#         if keys[pygame.K_UP]:
#             player.moveBaward()
while run:
    clock.tick(60)
    if not gameover:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.moveForward()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()        

pygame.quit()            
