from math import *
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
        
def draw_graph():
    for y in range(-10,11):
        for x in range(-10,12):
            if y == -10 and x == 0:
                graph.append("^")
            elif y == 0:
                if x == 0:
                    graph.append("0")
                elif x == 10:
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
zero_graph = draw_graph()
func_graph = draw_func(res)
print(res)
index=1
list1=""
for s in graph:
    if not(index%22==0):
        list1+=s
    else:
        print(list1)
        list1=""
    index+=1
