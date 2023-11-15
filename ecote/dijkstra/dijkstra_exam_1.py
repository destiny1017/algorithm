import heapq

INF = int(1e9)
n, m = map(int, input().split())
start_node = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    node, target, cost = map(int, input().split())
    graph[node].append((target, cost))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        min_distance, now_node = heapq.heappop(queue)
        if distance[now_node] < min_distance:
            continue

        for target, cost in graph[now_node]:
            cost += min_distance
            if cost < distance[target]:
                distance[target] = cost
                heapq.heappush(queue, (cost, target))


dijkstra(start_node)


for i in range(1, n+1):
    print("INF" if distance[i] == INF else distance[i])
