"""
Lab 2 template
"""

def read_incidence_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the incidence matrix of a given graph
    """
    vertices = set()
    edges = []
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    data = data[1:-1]

    for line in data:
        line = line.strip(';').split()
        start = int(line[0])
        end = int(line[-1])

        vertices.add(start)
        vertices.add(end)

        edges.append((start, end))

    incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(len(vertices))]

    for i, edge in enumerate(edges):
        start, end = edge
        if start == end:
            incidence_matrix[start][i] = 2
        else:
            incidence_matrix[start][i] = 1
            incidence_matrix[end][i] = -1
    return incidence_matrix


def read_adjacency_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the adjacency matrix of a given graph
    """
    vertices = set()
    edges = []
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    data = data[1:-1]

    for line in data:
        line = line.strip(';').split()
        start = int(line[0])
        end = int(line[-1])

        vertices.add(start)
        vertices.add(end)

        edges.append((start, end))
        
    adjacency_matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]

    for i, edge in enumerate(edges):
        node1, node2 = edge
        if (node2,node1) in edges:
            adjacency_matrix[node2][node1]= 1
        elif (node1, node2) in edges:
            adjacency_matrix[node1][node2] = 1
    return adjacency_matrix


def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict: the adjacency dict of a given graph
    """
    vertices = set()
    edges = []
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    data = data[1:-1]

    for line in data:
        line = line.strip(';').split()
        start = int(line[0])
        end = int(line[-1])

        vertices.add(start)
        vertices.add(end)

        edges.append((start, end))

    adjacency_dict = {}
    for edge in edges:
        if edge[0] not in adjacency_dict:
            adjacency_dict[edge[0]] = []
        adjacency_dict[edge[0]].append(edge[1])
    return adjacency_dict


def iterative_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    dfs = set()
    stack = [start]
    dfs.add(start)
    while stack:
        vert = stack.pop()
        for adj_nodes in graph[vert]:
            if adj_nodes not in dfs:
                dfs.add(adj_nodes)
                stack.append(adj_nodes)
    return list(dfs)


def iterative_adjacency_matrix_dfs(graph: list[list], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    def get_adjacent_nodes(node):
        adj_nodes = set()
        for i, edge in enumerate(graph[node]):
            if edge:
                adj_nodes.add(i)
        return adj_nodes

    stack = [start]
    visited_nodes = {start}
    dfs = [start]

    while stack:
        curr_node = stack[-1]
        if curr_node not in visited_nodes:
            visited_nodes.add(curr_node)
            dfs.append(curr_node)
        adj_nodes = get_adjacent_nodes(curr_node)
        unvisited_adj_nodes = [node for node in adj_nodes if node not in visited_nodes]

        if unvisited_adj_nodes:
            stack.append(unvisited_adj_nodes[0])
        else:
            stack.pop()

    return dfs


def recursive_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, result)

    visited = set()
    result = []
    dfs(start, visited, result)
    return result


def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    def dfs(node: int, visited: set[int], result: list[int]) -> None:
        visited.add(node)
        result.append(node)
        for adjacent_node, is_connected in enumerate(graph[node]):
            if is_connected and adjacent_node not in visited:
                dfs(adjacent_node, visited, result)

    visited = set()
    result = []
    dfs(start, visited, result)
    return result


def iterative_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    visited = set()
    queue = [start]
    bfs = []
    visited.add(start)

    while queue:
        node = queue.pop(0)
        bfs.append(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return bfs


def iterative_adjacency_matrix_bfs(graph: list[list[int]], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    def get_adjacent_nodes(node):
        adj_nodes = set()
        for i, edge in enumerate(graph[node]):
            if edge:
                adj_nodes.add(i)
        return adj_nodes

    queue = [start]
    visited_nodes = {start}
    bfs = [start]

    while queue:
        curr_node = queue[0]
        visited_nodes.add(curr_node)
        if curr_node not in bfs:
            bfs.append(curr_node)

        adj_nodes = get_adjacent_nodes(curr_node)
        unvisited_adj_nodes = [node for node in adj_nodes if node not in visited_nodes]

        if unvisited_adj_nodes:
            queue += unvisited_adj_nodes
        queue.pop(0)

    return bfs


# def recursive_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
#     """
#     :param list[list] graph: the adjacency list of a given graph
#     :param int start: start vertex of search
#     :returns list[int]: the bfs traversal of the graph
#     >>> recursive_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
#     [0, 1, 2]
#     >>> recursive_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
#     [0, 1, 2, 3]
#     """
#     pass


# def recursive_adjacency_matrix_bfs(graph: list[list[int]], start: int) ->list[int]:
#     """
#     :param dict graph: the adjacency matrix of a given graph
#     :param int start: start vertex of search
#     :returns list[int]: the bfs traversal of the graph
#     >>> recursive_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
#     [0, 1, 2]
#     >>> recursive_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
#     [0, 1, 2, 3]
#     """
#     pass


def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0]])
    2
    """
    pass


def adjacency_dict_radius(graph: dict[int: list[int]]) -> int:
    """
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [1]})
    2
    """
    def bfs(start: int) -> int:
        """Perform BFS and return the eccentricity from the start node."""
        visited = {start: 0}
        queue = [start]
        max_distance = 0

        while queue:
            current = queue.pop(0)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited[neighbor] = visited[current] + 1
                    queue.append(neighbor)
                    max_distance = max(max_distance, visited[neighbor])

        if len(visited) != len(graph):
            return float('inf')

        return max_distance

    eccentricities = [bfs(node) for node in graph]
    return min(eccentricities)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
