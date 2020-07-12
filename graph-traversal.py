from collections import defaultdict

order = []
def dfs(visited, graph, node):
	if not visited[node]:
		global order
		order.append(node)
		visited[node] = True
		for neighbour in graph[node]:
			dfs(visited, graph, neighbour)


def dfs_itr(graph, starting_node):
	visited = [False] * len(graph)

	stack = [starting_node]
	order = []
	while stack:
		node = stack.pop(-1)
		if not visited[node]:
			visited[node] = True
			order.append(node)
			for n in graph[node]:
				stack.append(n)

	return order


def bfs(graph, starting_node):
	queue = [starting_node]
	visited = [False] * len(graph)
	order = []
	while queue:
		node = queue.pop(0)
		if not visited[node]:
			visited[node] = True
			order.append(node)
			for n in graph[node]:
				queue.append(n)

	return order



n = int(input())

graph = defaultdict(list)

starting_node = 2
for i in range(n):
	x, y = map(int, input().split())
	if not starting_node: starting_node = x
	graph[x].append(y)
	# graph[y].append(x)

dfs([False] * len(graph), graph, starting_node)
print(f'DFS Recursive: {order}')

print(f'DFS Iterative: {dfs_itr(graph, starting_node)}')

print(f'BFS Iterative: {bfs(graph, starting_node)}')