from collections import deque

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'G'],
    'D': ['A', 'F'],
    'E': ['A', 'B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['C', 'F']
}

def bfs(start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighor in graph[node]:
            if neighor not in visited:
                visited.add(neighor)
                queue.append(neighor)
bfs('A')