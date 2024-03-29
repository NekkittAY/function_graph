from math import *
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("func_graph")
all_sprites=pygame.sprite.Group()
clock = pygame.time.Clock()
running = True
fps=60

class min_func:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def learn(self):
        for i in range(1000):
            m_func.update_c()
        for j in range(1000):
            m_func.update_a()
        for k in range(1000):
            m_func.update_b()
        for t in range(1000):
            m_func.update_d()
        
    def update_a(self):
        self.a0 = (self.a-0.1)
        self.a1 = (self.a+0.1)
        self.ra0 = MSE(self.a0,self.b,self.c,self.d)
        self.ra1 = MSE(self.a1,self.b,self.c,self.d)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.ma = min(self.ra0,self.ra1,self.rn)
        if self.ma==self.ra1:
            self.a=self.a1
        elif self.ma==self.ra0:
            self.a=self.a0

    def update_b(self):
        self.b0 = (self.b-0.1)
        self.b1 = (self.b+0.1)
        self.rb0 = MSE(self.a,self.b0,self.c,self.d)
        self.rb1 = MSE(self.a,self.b1,self.c,self.d)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.mb = min(self.rb0,self.rb1,self.rn)
        if self.mb==self.rb1:
            self.b=self.b1
        elif self.mb==self.rb0:
            self.b=self.b0

    def update_c(self):
        self.c00 = (self.c-1)
        self.c01 = (self.c+1)
        self.c10 = (self.c-2)
        self.c11 = (self.c+2)
        self.rc00 = MSE(self.a,self.b,self.c00,self.d)
        self.rc01 = MSE(self.a,self.b,self.c01,self.d)
        self.rc10 = MSE(self.a,self.b,self.c10,self.d)
        self.rc11 = MSE(self.a,self.b,self.c11,self.d)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.mc = min(self.rc00,self.rc01,self.rc10,self.rc11,self.rn)
        if self.mc==self.rc00:
            self.c=self.c00
        elif self.mc==self.rc01:
            self.c=self.c01
        elif self.mc==self.rc10:
            self.c=self.c10
        elif self.mc==self.rc11:
            self.c=self.c11


    def update_d(self):
        self.d0 = (self.d-0.1)
        self.d1 = (self.d+0.1)
        self.rd0 = MSE(self.a,self.b,self.c,self.d0)
        self.rd1 = MSE(self.a,self.b,self.c,self.d1)
        self.rn = MSE(self.a,self.b,self.c,self.d)
        self.md = min(self.rd0,self.rd1,self.rn)
        if self.md==self.rd1:
            self.d=self.d1
        elif self.md==self.rd0:
            self.d=self.d0

class Graph(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def count(self):
        clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        x=-10
        while x<=10:
            v0 = self.y[0]/self.x[0]
            v1 = self.y[1]/self.x[1]
            a = (v1-v0)/(self.x[1]-self.x[0])
            Vy = a*(x-self.x[0])+v0
            y = Vy*x
            dot=Dot(250+x*10,250-y*10,clr)
            all_sprites.add(dot)
            x+=0.0001
                   
                                        
class Roots(pygame.sprite.Sprite):
    def __init__(self,axis,pos,color):
        pygame.sprite.Sprite.__init__(self)
        if axis=="x":
            self.image=pygame.Surface((3,7))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.centerx = pos
            self.rect.centery = 250
        elif axis=="y":
            self.image=pygame.Surface((7,3))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.centerx = 250
            self.rect.centery = pos

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
    i=-10
    while i<=10:
        mass=""
        for j in func:
            if j == "x":
                mass+="("+str(i)+")"
            else:
                mass+=j
            i+=0.0001
        try:
          res1=eval(mass)
        except:
          res1=10000
        dot=Dot(250+i*10,250-res1*10,clr)
        all_sprites.add(dot)

def Calc_polar(func,clr):
    i=0
    while i<=1000:
        mass=""
        for j in func:
            if j == "p":
                mass+="radians("+str(i)+")"
            else:
                mass+=j
            i+=0.01
        try:
          res1=eval(mass)
        except:
          res1=10000
        y = sin(radians(i))*res1
        x = cos(radians(i))*res1
        dot=Dot(250+x*10,250-y*10,clr)
        all_sprites.add(dot)

def calc(func):
    result = []
    for i in range(-100,101):
        mass=""
        for s in func:
            if s=="x":
                mass+=str(i)
            else:
                mass+=s
        try:
            res=eval(mass)
            result.append(res)
        except:
            res=0
            result.append(res)
    return result

def prov_func(func,y,x):
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

def Calc_LP_NLP(func,clr):
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

def Calc_Newton(x,y,clr):
    i=-10
    while i<=10:
        res1=poly_Newton(x,y,i)
        i+=0.0001
        dot=Dot(250+i*10,250-res1*10,clr)
        all_sprites.add(dot)

def delta(X):
    if len(X)==2:
        return (y[X[1]]-y[X[0]])/(x[X[1]]-x[X[0]])
    else:
        return (delta(list(range(1,len(X))))-delta(list(range(0,len(X)-1))))/(x[X[len(X)-1]]-x[X[0]])

def poly_Newton(x,y,X):
    Y=0
    y0=y[0]
    Y+=y0
    t=2
    for i in range(len(x)-1):
        dy=delta(list(range(t+i)))
        dx=1
        for j in range(i+1):
            dx*=(X-x[j])
        dy*=dx
        Y+=dy
    return Y

def integral_rect(a,b,x0,func):
    res = 0
    while a<=b:
        res+=(prov_func(func,0,a)*x0)
        a+=x0
    return res

def integral_simpson(a,b,func):
    h=(b-a)/2
    roots=[]
    while a<=b:
        res1 = prov_func(func,0,a)
        roots.append(res1)
        a+=h
    res = 0
    res+=(roots[0]+roots[len(roots)-1])
    f0=0
    f1=0
    for i in range(len(roots)):
        if not(i==0) and not(i==(len(roots)-1)):
            if i%2==0:
                f0+=roots[i]
            else:
                f1+=roots[i]
    f0*=2
    f1*=4
    res+=f0
    res+=f1
    res*=(h/3)
    return res

def integral_dots(clr,a,b,func):
    y=0
    x=-10
    while y<=100:
        while x<=10:
            if x>=a and x<=b and y<=prov_func(func,0,x):
                dot=Dot(250+x*10,250-y*10,clr)
                all_sprites.add(dot)
            x+=0.1
        x=0
        y+=0.1

def method(clr):
    i=0
    j=0
    res=[]
    while i<=100:
        temp=[]
        while j<=100:
            for func1 in conditions:
                temp.append(prov_func(func1,i,j))
            if all(temp)==True:
                res.append([j,i])
                dot=Dot(250+j*10,250-i*10,clr)
                all_sprites.add(dot)
            temp=[]
            j+=0.1
        i+=0.1
        j=0
    return res

def MSE(a,b,c,d):
    res=0
    for i in range(0,len(f1)-1):
        try:
            sum1=(f1[i]-(a*(f2[i]+b)**c+d))**2
        except:
            sum1=(f1[i]-(a*(f2[i]+b+1)**c+d))**2
        res+=sum1
    res/=len(f1)
    return res

def MSE_prov(f1,f2):
    res=0
    for i in range(0,len(f1)-1):
        d1=(f1[i]-f2[i])**2
        res+=d1
    res/=len(f1)
    return res


def clean():
    all_sprites.empty()

def run():
    line = Line("y",250,250)
    all_sprites.add(line)
    line1 = Line("x",250,250)
    all_sprites.add(line1)
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.flip()
    img = pygame.image.save(screen,"screenshot.jpg")

def run_func(func):
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    Calc(func,clr)
    run()

def run_polar_func(func):
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    Calc_polar(func,clr)
    run()

def run_dots(Dots):
    x = []
    y = []
    dots = Dots.split()
    for i in range(len(dots)):
        roots=dots[i].split(',')
        x.append(float(roots[0]))
        y.append(float(roots[1]))
    for j in range(len(x)):
        clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        all_sprites.add(Roots('y',250-y[j]*10,clr))
        all_sprites.add(Roots('x',250+x[j]*10,clr))
    graph=Graph(x,y)
    graph.count()
    run()

def run_Newton(Dots):
    x = []
    y = []
    dots = Dots.split()
    for i in range(len(dots)):
        roots=dots[i].split(',')
        x.append(float(roots[0]))
        y.append(float(roots[1]))
    for j in range(len(x)):
        clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        all_sprites.add(Roots('y',250-y[j]*10,clr))
        all_sprites.add(Roots('x',250+x[j]*10,clr))
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    Calc_Newton(x,y,clr)
    run()

def run_approximation(func):
    global f1
    global f2
    f1 = calc(func)
    f2 = []
    for i in range(-100,101):
        f2.append(i)
    global m_func
    m_func = min_func(1,0,1,0)
    m_func.learn()
    function = f'm_func.a*(x+m_func.b)**m_func.c+m_func.d'
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    calc0 = Calc(func,(0,0,0))
    calc1 = Calc(function,clr)
    f0 = calc(function)
    res = MSE_prov(f1,f0)
    run()
    file = open('text.txt', 'w')
    file.write(str(res))

def run_integral_rect(a,b,func):
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    Calc(func,clr)
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    integral_dots(clr,int(a),int(b),func)
    res = integral_rect(int(a),int(b),0.001,func)
    file = open('text.txt', 'w')
    file.write(str(res))
    run()

def run_integral_simpson(a,b,func):
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    Calc(func,clr)
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    integral_dots(clr,int(a),int(b),func)
    res = integral_simpson(int(a),int(b),func)
    file = open('text.txt', 'w')
    file.write(str(res))
    run()

def run_ode_euler(x0,y0,func):
    h=0.0001
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    while x0<=10:
        dot=Dot(250+x0*10,250-y0*10,clr)
        all_sprites.add(dot)
        x0+=h
        y0 = y0+h*prov_func(func,y0,x0)
    run()

def run_ode_runge_kutta(x0,y0,func):
    h=0.0001
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    while x0<=10:
        dot=Dot(250+x0*10,250-y0*10,clr)
        all_sprites.add(dot)
        x0+=h
        k1 = prov_func(func,y0,x0)
        k2 = prov_func(func,y0+(h/2)*k1,x0+(h/2))
        k3 = prov_func(func,y0+(h/2)*k2,x0+(h/2))
        k4 = prov_func(func,y0+h*k3,x0+h)
        y0 = y0+(h/6)*(k1+2*k2+2*k3+k4)
    run()

def run_LP_NLP(function,func):
    global conditions
    global dict1
    func = func.split()
    conditions = []
    dict1=[">","<","=","y"]
    for i in range(len(func)):
        clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        conditions.append(func[i])
        calc0 = Calc_LP_NLP(func[i],clr)
    clr=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    result = method(clr)
    res = list(map(lambda x: prov_func(function,x[0],x[1]), result))
    run()
    file = open('text.txt', 'w')
    try:
        file.write(str(max(res)))
    except:
        file.write("None")

   
