from collections import deque

def BFS(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


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

print("Breadth First Traversal:")
BFS(graph, start)
