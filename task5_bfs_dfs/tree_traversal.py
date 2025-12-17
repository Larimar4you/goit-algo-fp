from task4_binary_heap.binary_heap import heap_to_tree, draw_tree


def generate_colors(n, base_color="#1296F0"):
    """
    Генерує n кольорів від темного до світлого відтінку на основі base_color.
    """
    # преобразуем base_color в RGB
    base_color = base_color.lstrip("#")
    r, g, b = (
        int(base_color[0:2], 16),
        int(base_color[2:4], 16),
        int(base_color[4:6], 16),
    )

    colors = []
    for i in range(n):
        factor = 0.5 + 0.5 * (i / max(1, n - 1))  # Від темного 0.5 до світлого 1.0
        new_r = min(int(r * factor), 255)
        new_g = min(int(g * factor), 255)
        new_b = min(int(b * factor), 255)
        colors.append(f"#{new_r:02X}{new_g:02X}{new_b:02X}")
    return colors


def dfs_order(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            # Спочатку правий, потім лівий, щоб лівий відвідувався раніше.
            stack.append(node.right)
            stack.append(node.left)
    return order


from collections import deque


def bfs_order(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order


def assign_colors_by_order(order, base_color="#1296F0"):
    colors = generate_colors(len(order), base_color)
    for node, color in zip(order, colors):
        node.color = color


heap = [0, 4, 1, 5, 10, 3]
root = heap_to_tree(heap)  # Використовуємо функцію з попередніх завдань.

# DFS
dfs_order = dfs_order(root)
assign_colors_by_order(dfs_order, "#FF0000")
draw_tree(root)

# BFS
root = heap_to_tree(heap)
bfs_order = bfs_order(root)
assign_colors_by_order(bfs_order, "#0000FF")
draw_tree(root)
