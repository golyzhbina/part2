def graph(filename: str) -> list:      # инициализация исходной матрицы

    with open(filename, "r", encoding="utf-8") as input_file:
        G = input_file.readlines()

    G = [list(map(lambda x: int(x.strip()), st.split())) for st in G]
    return G


start_graph = graph("data_for_d.txt")
from_vertex = 0

visited_v = [False] * len(start_graph)
values_of_v = [max(map(max, start_graph)) + 1] * len(start_graph)
values_of_v[from_vertex] = 0

while True:

    for v in range(len(start_graph[from_vertex])):

        if start_graph[from_vertex][v] == 0:
            continue

        if values_of_v[from_vertex] + start_graph[from_vertex][v] < values_of_v[v]:
            values_of_v[v] = values_of_v[from_vertex] + start_graph[from_vertex][v]

    visited_v[from_vertex] = True

    if not all(visited_v):
        lst1 = []
        for val in range(len(values_of_v)):
            if not visited_v[val]:
                lst1.append(list(enumerate(values_of_v))[val])
        from_vertex = min(lst1, key=lambda x: x[-1])[0]
    else:
        break

print(values_of_v)


