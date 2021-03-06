from tkinter import *
import copy
from matplotlib import pyplot as plt
import math
import numpy as np



def visual():
    vertexs = int(text.get())
    print(vertexs)

    edges = 0
    loops = 0

    g_matrix = [[0] * vertexs for i in range(vertexs)]

    user_input = (text1.get()).split(",")
    for i in range(len(user_input)):
        # a, b = list(map(int, user_input.split()))
        l = user_input[i].split(" ")
        a = int(l[0])
        b = int(l[1])
        if not g_matrix[a - 1][b - 1]:
            g_matrix[a - 1][b - 1] = 1
            edges += 1
            if a == b:
                loops += 1

    visualze(g_matrix)

def path(a, b, m_set, used_points=[]):
    used_points = used_points.copy()
    used_points += [a]
    for u in range(len(m_set[a])):
        if m_set[a][u]:
            if u == b:
                return True
            elif u not in used_points and path(u, b, m_set, used_points):
                return True
    return False


def mirror(matr):
    m = copy.deepcopy(matr)
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = int(m[i][j] or m[j][i])
    return m


def print_matrix(matr):
    for r in matr:
        for c in r:
            print("%2d" % c, end='')
        print()


def visualze(matr, graph_type='graph'):
    n = len(matr)
    points = np.linspace(0, 2 * math.pi, n + 1)
    x = np.cos(points)
    y = np.sin(points)

    d = 0.93  # used to accurate arrow length
    plt.axis('off')
    plt.scatter(x, y, linewidth=5, alpha=0.8, color='black')
    for i in range(len(matr)):
        for j in range(len(matr)):
            if matr[i][j] == 1 and i == j:
                plt.scatter([x[i]], [y[i]], linewidth=15, color='red', alpha=0.4)
            elif matr[i][j] == 1:
                if graph_type == 'graph':
                    plt.plot([x[i], x[j]], [y[i], y[j]], linewidth=3, alpha=0.3, color='black')
                else:
                    plt.arrow(x[i], y[i], (x[j] - x[i]) * d, (y[j] - y[i]) * d, width=0.02, alpha=0.5)
    plt.show()


def componenta(vertex, matr):
    res = {vertex}
    for p in range(len(matr)):
        if p != vertex and path(vertex, p, matr):
            res.add(p)
    return res


def directed():

    vertexs = int(text.get())
    print(vertexs)

    edges = 0
    loops = 0

    g_matrix = [[0] * vertexs for i in range(vertexs)]

    user_input = (text1.get()).split(",")
    for i in range(len(user_input)):
        # a, b = list(map(int, user_input.split()))
        l = user_input[i].split(" ")
        a = int(l[0])
        b = int(l[1])
        print(a,b)
        if not g_matrix[a - 1][b - 1]:
            g_matrix[a - 1][b - 1] = 1
            g_matrix[b - 1][a - 1] = 1
            edges += 1
            if a == b:
                loops += 1
    #print(vertexs, loops, edges)

    degree = max([sum(r) for r in g_matrix])

    connected = True

    for i in range(vertexs):
        for j in range(vertexs):
            if not path(i, j, g_matrix):
                connected = False

    if connected:
        label2.configure(text="?????????????? ????????\n")
    else:
        label2.configure(text="?????????????????? ????????\n")

    res3 = "???????????????????? ???????????? = {}".format(vertexs)
    label3.configure(text=res3)
    res4 = "???????????????????? ?????????? = {}".format(edges)
    label4.configure(text=res4)
    res5 = "???????????????????? ???????????? = {}".format(loops)
    label5.configure(text=res5)
    res6 = "???????????????????????? ?????????????? ?????????????? = {}".format(degree)
    label6.configure(text=res6)

    components = []
    set_vertexes = set(range(vertexs))
    while set_vertexes:
        v = set_vertexes.pop()
        c = componenta(v, g_matrix)
        if not c:
            c = {v}
        set_vertexes -= c
        components += [c]

    res7 = "?????????????????? ?????????????????? = {}".format(len(components))
    label7.configure(text=res7)
    for c in components:
         res8=set(map(lambda x: x + 1, c))
         label8.configure(text=res8)
    label9.configure(text="???????????????? ???????? (?????????????? `????`)")
    butt1 = Button(grap,  # ???????????????????????? ????????
                  text="????",  # ?????????????? ???? ????????????
                  width=30, height=2,  # ???????????? ?? ????????????
                  bg="white", fg="black",
                  command=visual)
    butt1.grid(column=0, row=15)


grap = Tk()
grap.title('DM 3 TASK')
grap.geometry('600x600')
grap.configure(bg='#FFAAAA')
label = Label(grap, text="?????????????? ???????????????????? ????????????")
label.grid(column=0, row=0)
text = Entry(grap, width=10)
text.grid(column=0, row=1)
label1 = Label(grap, text="?????????????? ???????? ???????????? ?????? ?? ??????????????. ????????????:1 2,3 4,5 6")
label1.grid(column=0, row=2)
text1 = Entry(grap, width=10)
text1.grid(column=0, row=3)
butt = Button(grap,  # ???????????????????????? ????????
              text="Click me",  # ?????????????? ???? ????????????
              width=30, height=2,  # ???????????? ?? ????????????
              bg="white", fg="black",
              command=directed)
butt.grid(column=0, row=4)
label2 = Label(grap)
label2.grid(column=0, row=5)
label3 = Label(grap)
label3.grid(column=0, row=6)
label4 = Label(grap)
label4.grid(column=0, row=7)
label5 = Label(grap)
label5.grid(column=0, row=8)
label6 = Label(grap)
label6.grid(column=0, row=9)
label7 = Label(grap)
label7.grid(column=0, row=10)
label8 = Label(grap)
label8.grid(column=0, row=11)
label9 = Label(grap)
label9.grid(column=0, row=12)

grap.mainloop()