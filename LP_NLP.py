from math import *
import random
import pygame 

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("func_graph")
all_sprites=pygame.sprite.Group()
clock = pygame.time.Clock()
running = True
fps=60

class Line(pygame.sprite.Sprite):
    def __init__(self,pos,x,y):
        pygame.sprite.Sprite.__init__(self)
        if pos=="x":
            self.image=pygame.Surface((3,400))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        elif pos=="y":
            self.image=pygame.Surface((400,3))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            
class Dot(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.surface.Surface((5,5))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
            
def Calc(func,clr):
    i=0
    while i<=100:
        mass=""
        for j in func:
            if j == "x":
                mass+=str(i)
            elif j in dict1:
                pass
            else:
                mass+=j
            i+=0.001
        try:
          res1=eval(mass)
        except:
          res1=10000
        dot=Dot(250+i*10,250-res1*10,clr)
        all_sprites.add(dot)

def calc(func,y,x):
    mass=""
    for j in func:
        if j == "x":
            mass+=str(x)
        elif j == "y":
            mass+=str(y)
        else:
            mass+=j
    try:
        res1=eval(mass)
    except:
        res1=False
    return res1

def method(clr):
    i=0
    j=0
    res=[]
    while i<=100:
        temp=[]
        while j<=100:
            for func1 in conditions:
                temp.append(calc(func1,i,j))
            if all(temp)==True:
                res.append([j,i])
                dot=Dot(250+j*10,250-i*10,clr)
                all_sprites.add(dot)
            temp=[]
            j+=0.1
        i+=0.1
        j=0
    return res
            
function = str(input("f(x) = "))
num = int(input("number of function: "))
conditions = []
dict1=[">","<","=","y"]
for i in range(num):
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    func0 = input()
    conditions.append(func0)
    calc0 = Calc(func0,clr)
result = method(clr)
res = list(map(lambda x: calc(function,x[0],x[1]), result))
print(max(res))


line = Line("y",250,250)
all_sprites.add(line)
line1 = Line("x",250,250)
all_sprites.add(line1)

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
