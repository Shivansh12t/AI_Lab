from collections import deque

def tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    queue = deque([(start,[start],0)]) # [(current_node, path, cost_so_far)]
    shortest_path = None
    shortest_distance = 10000

    while queue:
        current_node, path, total_cost = queue.popleft()

        if len(path) == n and graph[current_node][start] != 0:
            path.append(start)
            total_cost += graph[current_node][start]
            if total_cost < shortest_distance:
                shortest_path = path
                shortest_distance = total_cost
            continue

        for neighbours in range(n):
            if (neighbours not in path) and (not visited[neighbours]) and graph[current_node][neighbours] != 0:
                visited[neighbours] = True
                new_path = path + [neighbours]
                new_cost = total_cost + graph[current_node][neighbours]
                print((neighbours,new_path,new_cost))
                queue.append((neighbours,new_path,new_cost))
                visited[neighbours] = False # Backtrack

    return shortest_path,shortest_distance

# -- main --
graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

starting_node = int(input("Enter the starting node :"))

shortest_path, shortest_distance = tsp(graph, starting_node)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)
