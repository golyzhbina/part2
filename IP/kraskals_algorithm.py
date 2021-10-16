import networkx
from numpy import array
import numpy as np
import copy
import matplotlib.pyplot as plt


def init_a_matrix(filename: str) -> list:      # инициализация исходной матрицы

    with open(filename, "r", encoding="utf-8") as input_file:
        a_matrix = input_file.readlines()[1:]

    a_matrix = [list(map(lambda x: int(x.strip()), st.split())) for st in a_matrix]
    return a_matrix


def func_r_matrix(a_matrix: list) -> list:  # вычисление матрицы смежности

    n = len(a_matrix)
    a_matrix = [list(map(lambda x: 1 if x != 0 else 0, a_matrix[i])) for i in range(len(a_matrix))]
    r_matrix_1 = copy.deepcopy(a_matrix)
    r_matrix = array(list(map(array, a_matrix)))
    r_matrix_1 = array(list(map(array, r_matrix_1)))

    for i in range(2, n):
        r_matrix += np.dot(r_matrix, r_matrix_1)

    r_matrix = list(map(list, r_matrix))
    for i in range(len(r_matrix)):
        r_matrix[i] = list(map(lambda x: 1 if x > 0 else 0, r_matrix[i]))

    return list(map(list, r_matrix))


def init_graph_vertexes(filename: str) -> list:     # инициализация вершин матрицы
    with open(filename, "r", encoding="utf-8") as input_file:
        graph_vertexes = input_file.readline().split()
        graph_vertexes = list(map(lambda x: x.strip(), graph_vertexes))
    return graph_vertexes


def min_val_search():   # поиск ребра с минимальным весом

    global start_max
    global start_a_matrix_copy
    global lst_min_vals

    n = len(start_a_matrix_copy)
    old_min_val = (start_max + 1, 0, 0)

    for i in range(n):
        new_min_val = min(filter(lambda x: x > 0, start_a_matrix_copy[i]))
        new_min_val = (new_min_val, i, start_a_matrix_copy[i].index(new_min_val))
        if old_min_val[0] > new_min_val[0]:
            old_min_val = new_min_val

    start_a_matrix_copy[old_min_val[1]][old_min_val[2]] = start_max + 1
    start_a_matrix_copy[old_min_val[2]][old_min_val[1]] = start_max + 1
    lst_min_vals.append(old_min_val)

    return old_min_val


def search_cycle(a_matrix_old):
    global lst_min_vals
    global final_result
    ribs = []
    ribs_cycle = []

    a_matrix_new = copy.deepcopy(a_matrix_old)

    for i in range(len(a_matrix_old)):
        a_matrix_old[i] = list(map(lambda x: x if i < a_matrix_old[i].index(x) else 0, a_matrix_old[i]))

    for i in range(len(a_matrix_old)):
        ribs_i = list(filter(lambda x: x != 0,
                             map(lambda x: (i, a_matrix_old[i].index(x)) if x != 0 else 0, a_matrix_old[i])))
        ribs.extend(ribs_i)

    for rib in ribs:

        a_matrix_new[rib[0]][rib[1]] = 0
        a_matrix_new[rib[1]][rib[0]] = 0
        r_matrix_new = func_r_matrix(a_matrix_new)

        if r_matrix_new == final_result:
            ribs_cycle.append((old_a_matrix[rib[0]][rib[1]], rib[0], rib[1]))

        a_matrix_new[rib[0]][rib[1]] = a_matrix_old[rib[0]][rib[1]]
        a_matrix_new[rib[1]][rib[0]] = a_matrix_old[rib[0]][rib[1]]

    for i in range(len(ribs_cycle)):
        max_rib = max(ribs_cycle, key=lambda x: x[0])
        a_matrix_new[max_rib[1]][max_rib[2]] = 0
        a_matrix_new[max_rib[2]][max_rib[1]] = 0
        r_matrix_new = func_r_matrix(a_matrix_new)

        if r_matrix_new != final_result:
            a_matrix_new[max_rib[1]][max_rib[2]] = a_matrix_old[max_rib[1]][max_rib[2]]
            a_matrix_new[max_rib[2]][max_rib[1]] = a_matrix_old[max_rib[1]][max_rib[2]]
        else:
            a_matrix_new[max_rib[1]][max_rib[2]] = 0
            a_matrix_new[max_rib[2]][max_rib[1]] = 0

        ribs_cycle[ribs_cycle.index(max_rib)] = (0, 0, 0)

    return a_matrix_new


start_graph_vertex = init_graph_vertexes("start_data_graph.txt")
start_a_matrix = init_a_matrix("start_data_graph.txt")

start_a_matrix_copy = copy.deepcopy(start_a_matrix)
start_max = max(map(max, start_a_matrix_copy))

lst_min_vals = list()
tree = set()

old_a_matrix = [[0 for _ in range(len(start_a_matrix))] for _ in range(len(start_a_matrix))]
old_r_matrix = [[0 for _ in range(len(start_a_matrix))] for _ in range(len(start_a_matrix))]
new_a_matrix = [[0 for _ in range(len(start_a_matrix))] for _ in range(len(start_a_matrix))]

final_result = [[1] * len(start_a_matrix) for i in range(len(start_a_matrix))]

while True:
    if old_r_matrix == final_result and len(lst_min_vals) == len(start_graph_vertex) - 1:
        break
    elif old_r_matrix == final_result and len(lst_min_vals) > len(start_graph_vertex) - 1:
        old_a_matrix = search_cycle(old_a_matrix)
        break

    min_val = min_val_search()
    old_a_matrix[min_val[1]][min_val[2]] = min_val[0]
    old_a_matrix[min_val[2]][min_val[1]] = min_val[0]
    old_r_matrix = func_r_matrix(old_a_matrix)


for i in range(len(old_a_matrix)):
    old_a_matrix[i] = list(map(lambda x: x if i < old_a_matrix[i].index(x) else 0, old_a_matrix[i]))

for i in range(len(old_a_matrix)):
    ways = filter(lambda x: x != 0, old_a_matrix[i])
    for way in ways:
        tree.add((start_graph_vertex[i], start_graph_vertex[old_a_matrix[i].index(way)], way))

G = networkx.Graph()
G.add_weighted_edges_from(tree)

networkx.draw(G, node_color='red',  node_size=1000, with_labels=True)
plt.show()
