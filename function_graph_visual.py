from math import *
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
            self.image=pygame.Surface((1,y))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        elif pos=="y":
            self.image=pygame.Surface((y,1))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            
class Dot(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.surface.Surface((5,5))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
            
def Calc(func):
    for i in range(-10,11):
        mass=""
        for j in func:
            if j == "x":
                mass+=str(i)
            else:
                mass+=j
        try:
            res1=eval(mass)
            res.append(res1)
            print(res1)
        except:
            res.append(0)
        #dot=Dot(250+i*10,250-res1*10)
        #all_sprites.add(dot)

def Calc_draw(func):
    i=-10
    while i<=10:
        mass=""
        for j in func:
            if j == "x":
                mass+=str(i)
            else:
                mass+=j
            i+=0.0001
        try:
          res1=eval(mass)
        except:
          res1=10000
        dot=Dot(250+i*10,250-res1*10)
        all_sprites.add(dot)
        
def draw_graph():
    for y in range(-10,11):
        for x in range(-10,12):
            if y == -10 and x == 0:
                graph.append("^")
            elif y == 0:
                if x == 0:
                    graph.append("0")
                elif x == 11:
                    graph.append(">")
                else:
                    graph.append("-")
            elif x == 0:
                graph.append("|")
            else:
                graph.append(" ")
    return graph

def draw_func(result):
    index=0
    for i in range(-10,11):
        for j in range(-10,11):
            if int(result[index])==j:
                formula=22*(10-j)+(20-(10-i))
                graph[formula] = "*"
        index+=1
    return graph

res=[]
graph = []
func = str(input("y = "))
calc = Calc(func)
calc1 = Calc_draw(func)
zero_graph = draw_graph()
func_graph = draw_func(res)
print(res)
index=0
list1=""
for s in graph:
    if not(index%22==0):
        list1+=s
    else:
        print(list1)
        list1=""
    index+=1
    
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
