import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def heap_to_tree(heap):
    if not heap:
        return None

    nodes = [Node(value) for value in heap]

    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap):
            nodes[i].left = nodes[left]
        if right < len(heap):
            nodes[i].right = nodes[right]

    return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)


def draw_tree(root, title):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_colors(n, base_color="#1296F0"):
    base_color = base_color.lstrip("#")
    r, g, b = (
        int(base_color[0:2], 16),
        int(base_color[2:4], 16),
        int(base_color[4:6], 16),
    )

    colors = []
    for i in range(n):
        factor = 0.4 + 0.6 * (i / max(1, n - 1))
        colors.append(f"#{int(r*factor):02X}{int(g*factor):02X}{int(b*factor):02X}")
    return colors


def dfs(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)

    return order


def bfs(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)

    return order


def color_nodes(order, base_color):
    colors = generate_colors(len(order), base_color)
    for node, color in zip(order, colors):
        node.color = color


heap = [0, 4, 1, 5, 10, 3]

root = heap_to_tree(heap)
dfs_order = dfs(root)
color_nodes(dfs_order, "#1296F0")
draw_tree(root, "DFS traversal")

root = heap_to_tree(heap)
bfs_order = bfs(root)
color_nodes(bfs_order, "#1296F0")
draw_tree(root, "BFS traversal")
