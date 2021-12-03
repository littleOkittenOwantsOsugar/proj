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
    visualze(g_matrix, "directed")

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
        print("a=", a, "B=", b)
        if not g_matrix[a - 1][b - 1]:
            g_matrix[a - 1][b - 1] = 1
            edges += 1
            if a == b:
                loops += 1
    print(vertexs, loops, edges)

    outcome_degree = max([sum(r) for r in g_matrix])
    income_degree = max([sum([g_matrix[i][j] for i in range(vertexs)]) for j in range(vertexs)])

    connected = True
    unilaterally = True
    strongly = True

    g_mmatrix = mirror(g_matrix)

    for i in range(vertexs):
        for j in range(vertexs):
            if i != j:
                if not (path(i, j, g_matrix) and path(j, i, g_matrix)):
                    strongly = False
                if not (path(i, j, g_matrix) or path(j, i, g_matrix)):
                    unilaterally = False
                if not (path(i, j, g_mmatrix) or path(j, i, g_mmatrix)):
                    connected = False

    if strongly:
        label2.configure(text="Cильно связный граф\n")
    elif unilaterally:
        label2.configure(text="Односторонне связный\n")
    elif connected:
        label2.configure(text="Связный граф\n")
    else:
        label2.configure(text="Несвязный граф\n")

    res3 = "Количество вершин = {}".format(vertexs)
    label3.configure(text=res3)
    res4 = "Количество ребер = {}".format(edges)
    label4.configure(text=res4)
    res5 = "Количество петель = {}".format(loops)
    label5.configure(text=res5)
    res6 = "Максимальная степень исхода = {}".format(outcome_degree)
    label6.configure(text=res6)
    res7 = "Максимальная степень захода = {}".format(income_degree)
    label7.configure(text=res7)
    label8.configure(text="Показать граф (Нажмите `да`)")
    butt1 = Button(grap,  # родительское окно
                  text="ДА",  # надпись на кнопке
                  width=30, height=2,  # ширина и высота
                  bg="white", fg="black",
                  command=visual)
    butt1.grid(column=0, row=12)


grap = Tk()
grap.title('DM 3 TASK')
grap.geometry('600x600')
grap.configure(bg='#FFAAAA')
label = Label(grap, text="Введите количество вершин")
label.grid(column=0, row=0)
text = Entry(grap, width=10)
text.grid(column=0, row=1)
label1 = Label(grap, text="Введите пары вершин как в примере. Пример:1 2,3 4,5 6")
label1.grid(column=0, row=2)
text1 = Entry(grap, width=10)
text1.grid(column=0, row=3)
butt = Button(grap,  # родительское окно
              text="Click me",  # надпись на кнопке
              width=30, height=2,  # ширина и высота
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

grap.mainloop()