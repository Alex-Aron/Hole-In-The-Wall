import pygame, numpy, sys
import numpy as np
WIDTH = 1300
HEIGHT = 900

pygame.init()

class borders:#Holes in the wall for the player to fit through
    def __init__(self, x_p, y_p, gap_size=100) -> None:
        self.x_p = x_p
        self.y_p = y_p
        self.body = pygame.Rect(x_p, y_p, 40, 200)

    def getRect(self):
        return self.body
    def getPos(self):
        return (self.x_p,self.y_p)

    def getTop(self):
        return self.y_p

    def getBottom(self):
        return self.body.bottom

    def setTop(self, ypos):
        #self.body.top = ypos
        self.y_p = ypos

    def setBottom(self, ypos):
        #self.body.bottom = ypos
        self.y_p = ypos

    def move_left(self, speed):
        self.x_p -= speed
        self.body.move_ip(-speed,0)

        

class player:
    def __init__(self,x_p, y_p) -> None:
        self.x_p = x_p
        self.y_p = y_p
        self.body = pygame.Rect(x_p,y_p,5,5)
        self.speed = 0

    def getPos(self):
        return (self.x_p,self.y_p)
    
    def getTop(self):
        return self.y_p
    
    def getBottom(self):
        return self.body.bottom

    def setTop(self, ypos):
        #self.body.top = ypos
        self.y_p = ypos

    def setBottom(self, ypos):
        #self.body.bottom = ypos
        self.y_p = ypos

    def move_up(self):
        self.y_p -= 1
    
    def move_down(self):
        self.y_p += 1


def run():
    pass
def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True
    user = player(40, 300)
    top_border = borders(1200.0, 0)
    bottom_border = borders(1200.0, 500)
    speed = 1
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        screen.fill("black")    
        pygame.draw.circle(screen, "blue", user.getPos(), 30)
        pygame.draw.rect(screen, "white", top_border.getRect(), 50)
        pygame.draw.rect(screen, "white", bottom_border.getRect(), 50)

        if keys[pygame.K_w]:
            user.move_up()
        if keys[pygame.K_s]:
            user.move_down()
        if user.getTop() <= 15:
            user.setTop(15)
        if user.getTop() >= HEIGHT-15:
            user.setBottom(HEIGHT-15)
        top_border.move_left(1)
        bottom_border.move_left(1)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()