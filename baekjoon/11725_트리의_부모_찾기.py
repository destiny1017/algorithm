# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = []  # 노드 연결 상태를 나타낼 그래프
result = []  # 각 노드의 부모가 담길 리스트


# null 참조 방지를 위한 default data 세팅
for i in range(n+1):
    graph.append([])
    result.append(0)

# 노드 연결 정보 추가
for i in range(1, n):
    f, s = map(int, sys.stdin.readline().split())
    graph[f].append(s)
    graph[s].append(f)

# print(graph)

# 각 노드의 그래프 별로 요소 순회를 하며 현재 val이 부모 노드가 아니면 val을 부모로 지정
def dfs(val, parent):
    for i in graph[val]:
        if i != parent[val]:
            # print(i, val)
            parent[i] = val
            dfs(i, parent)


dfs(1, result)

for i in result[2:]:
    print(i)

print("\n".join(str(x) for x in result))
