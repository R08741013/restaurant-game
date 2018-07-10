import pygame
from UI import *
pygame.init()
info = pygame.display.Info()
screenWidth, screenHeight = 700, 525
width, height = 400, 300
#window = pygame.display.set_mode((width, height))
screen = pygame.Surface((width, height))
window = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

quitted = False
first = True
 
white = (255, 255, 255)
black = (0, 0, 0)

me = pygame.image.load('./Sources/Something.png').convert()
tableTex = pygame.image.load('./Sources/Table.png').convert()

meW, meH = me.get_width(), me.get_height()

t = pygame.Rect(0, 0, width, 1)
l = pygame.Rect(0, 0, 1, height)
b = pygame.Rect(0, height, width, 1)
r = pygame.Rect(width, 0, 0, height)

class point:
    def __init__(self, x = 0, y = 0): #Default is set x and y to 0
        self.x, self.y = x, y
    def add(self, p):
        self.x += p.x
        self.y += p.y
    def addX(self, num):
        self.x += num
    def addY(self, num):
        self.y += num
    def sub(self, p):
        self.x -= p.x
        self.y -= p.y
    def mult(self, num):
        self.x *= num
        self.y *= num
    def limit(self, num):
        if self.x > num: self.x = num
        elif self.x < -num: self.x = -num
        elif self.y > num: self.y = num
        elif self.y < -num: self.y = -num

class table:
    def __init__(self, x, y, num):
        self.tableNum = num
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 270, 145)
        self.occupied = False
        self.numCustomers = 0
        
    def display(self):
        pass
        '''
        if not self.occupied:
            screen.blit(tableTex, (self.x, self.y))
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)
        else:
            pygame.draw.rect(screen, (127, 0, 0), self.rect, 0)'''

    def collide(self, rectangle):
        if self.rect.colliderect(rectangle):
            return True
        else:
            return False

    def dosomething(self):
        pass

def game():
    global first, meP, meV, meA, meRect, tables, firsthit
    if first:
        first = False
        meP = point(width/2, height/2)
        meV = point()
        meA = point()
        meRect = pygame.Rect(width/2, height/2, meW, meH)
        tables = []
        tables.append(table(0, 0, 1))
        #tables.append(table(0, 250, 2))
        #tables.append(table(0, 500, 3))
        #tables.append(table(0, 750, 4))

    COL = False
    speed = 0.01
    keysPressed = pygame.key.get_pressed()
    #Keys
        
    meV.limit(7)
    meV.add(meA)
    meP.add(meV)
    
    if meP.x < 0:
        meP.x = 1
        meV.x = 0
    if meP.x > width - meW:
        meP.x = width - meW - 1
        meV.x = 0
    if meP.y < 0:
        meP.y = 1
        meV.y = 0
    if meP.y > height - meH:
        meP.y = height - meH - 1
        meV.y = 0
    #meV.limit(0)
    meRect = pygame.Rect(meP.x, meP.y, meW, meH)
    meA.mult(0)
    screen.blit(me, (meP.x, meP.y))
    #pygame.draw.rect(screen, (0, 255, 0), meRect, 1)
    for t in tables:
            t.display()
            '''
        if t.collide(meRect):
            COL = True
            if t.occupied:
                meV.mult(0)
            else:
                meV.x = 0
            t.dosomething()'''
    if not COL:
        if keysPressed[pygame.K_w] == 1:
            meA.addY(-speed)
        if keysPressed[pygame.K_a] == 1:
            meA.addX(-speed)
        if keysPressed[pygame.K_s] == 1:
            meA.addY(speed)
        if keysPressed[pygame.K_d] == 1:
            meA.addX(speed)
        if keysPressed[pygame.K_o] == 1:
            tables[0].occupied = True
        if keysPressed[pygame.K_p] == 1:
            tables[0].occupied = False

while not quitted:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
            quitted = True
        
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill(white)
    game()
    window.blit(pygame.transform.scale(screen, (screenWidth, screenHeight)).convert(), (0, 0))
    pygame.display.update()
    clock.tick(480)

pygame.quit()
quit()
