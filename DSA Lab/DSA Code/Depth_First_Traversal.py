def DFS(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)

        for neighbour in graph[vertex]:
            DFS(graph, neighbour, visited)


graph = {}

n = int(input("Enter number of vertices: "))

print("Enter vertices:")
vertices = input().split()

for vertex in vertices:
    graph[vertex] = []

e = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for i in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter starting vertex: ")

visited = set()

print("Depth First Traversal:")
DFS(graph, start, visited)
