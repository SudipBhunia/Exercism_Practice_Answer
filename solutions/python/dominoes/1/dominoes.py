from collections import defaultdict, Counter

def can_chain(dominoes):
    if not dominoes:
        return []
    
    graph = defaultdict(list)
    degree = Counter()
    
    for i, (a, b) in enumerate(dominoes):
        graph[a].append((b, i))
        graph[b].append((a, i))
        degree[a] += 1
        degree[b] += 1
    
    odd_degree_nodes = [node for node, deg in degree.items() if deg % 2 == 1]
    
    if len(odd_degree_nodes) not in [0, 2]:
        return None
    
    start = odd_degree_nodes[0] if odd_degree_nodes else list(degree.keys())[0]
    
    path = []
    used = set()
    
    def dfs(node):
        for neighbor, domino_idx in graph[node]:
            if domino_idx not in used:
                used.add(domino_idx)
                dfs(neighbor)
                a, b = dominoes[domino_idx]
                if node == b:
                    path.append((b, a))
                else:
                    path.append((a, b))
    
    dfs(start)
    
    if len(path) != len(dominoes):
        return None
    
    path.reverse()
    
    for i in range(len(path) - 1):
        if path[i][1] != path[i + 1][0]:
            return None
    
    if path[0][0] != path[-1][1]:
        return None
    
    return path