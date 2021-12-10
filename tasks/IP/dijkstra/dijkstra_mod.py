def graph(filename: str):      # инициализация исходной матрицы

    with open(filename, "r", encoding="utf-8") as input_file:
        G = input_file.readlines()[1:]
        from_to = [st.strip() for st in G[-1]]

    G = [list(map(lambda x: int(x.strip()), st.split())) for st in G[:-1]]
    return G, from_to


def init_graph_vertexes(filename: str) -> list:     # инициализация вершин матрицы
    with open(filename, "r", encoding="utf-8") as input_file:
        graph_vertexes = input_file.readline().split()
        graph_vertexes = list(map(lambda x: x.strip(), graph_vertexes))
    return graph_vertexes


start_graph, from_to_v = graph("data_for_d_mod.txt")
name_of_v = init_graph_vertexes("data_for_d_mod.txt")
from_vertex = name_of_v.index(from_to_v[0])
to = name_of_v.index(from_to_v[-1])

visited_v = [False] * len(start_graph)
values_of_v = [max(map(max, start_graph)) + 1] * len(start_graph)
values_of_v[from_vertex] = 0
ways = {name_of_v[i]: " " for i in range(len(name_of_v))}

while True:

    for v in range(len(start_graph[from_vertex])):

        if start_graph[from_vertex][v] == 0:
            continue

        if values_of_v[from_vertex] + start_graph[from_vertex][v] <= values_of_v[v]:
            values_of_v[v] = values_of_v[from_vertex] + start_graph[from_vertex][v]
            ways[name_of_v[v]] = name_of_v[from_vertex]

    visited_v[from_vertex] = True

    if not all(visited_v):
        lst1 = []
        for val in range(len(values_of_v)):
            if not visited_v[val]:
                lst1.append(list(enumerate(values_of_v))[val])
        from_vertex = min(lst1, key=lambda x: x[-1])[0]
    else:
        break

way = str()
to = name_of_v[to]
while True:
    if to == " ":
        break
    way += to
    to = ways[to]

print(way[::-1])
