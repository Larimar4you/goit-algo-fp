import matplotlib.pyplot as plt
import math


def draw_square(x, y, size, angle):
    """Малює квадрат з нижньої лівої точки"""
    points = []
    for dx, dy in [(0, 0), (size, 0), (size, size), (0, size), (0, 0)]:
        rx = x + dx * math.cos(angle) - dy * math.sin(angle)
        ry = y + dx * math.sin(angle) + dy * math.cos(angle)
        points.append((rx, ry))

    xs, ys = zip(*points)
    plt.plot(xs, ys, color="green")


def pythagoras_tree(x, y, size, angle, depth):
    if depth == 0:
        return

    draw_square(x, y, size, angle)

    new_size = size * math.sqrt(2) / 2

    # Лівий квадрат
    x1 = x + size * math.cos(angle)
    y1 = y + size * math.sin(angle)
    pythagoras_tree(x1, y1, new_size, angle + math.pi / 4, depth - 1)

    # Правий квадрат
    x2 = x1 + new_size * math.cos(angle + math.pi / 4)
    y2 = y1 + new_size * math.sin(angle + math.pi / 4)
    pythagoras_tree(x2, y2, new_size, angle - math.pi / 4, depth - 1)


def main():
    depth = int(input("Введіть рівень рекурсії (наприклад 8–12): "))

    plt.figure(figsize=(8, 8))
    plt.axis("equal")
    plt.axis("off")

    # Початковий квадрат
    pythagoras_tree(x=0, y=0, size=1, angle=0, depth=depth)

    plt.show()


if __name__ == "__main__":
    main()
