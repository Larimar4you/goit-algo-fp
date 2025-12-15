import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

WIDTH, HEIGHT = 400, 400
MAX_ITER = 100

fig, ax = plt.subplots()
ax.axis("off")

image = ax.imshow(
    np.zeros((HEIGHT, WIDTH)),
    cmap="turbo",  # 🔥 красивая палитра
    vmin=0,
    vmax=MAX_ITER,
    animated=True,
)


def mandelbrot(frame):
    scale = 3 * (0.97**frame)
    cx, cy = -0.5, 0

    x = np.linspace(cx - scale, cx + scale, WIDTH)
    y = np.linspace(cy - scale, cy + scale, HEIGHT)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)

    output = np.zeros(C.shape)

    for i in range(MAX_ITER):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        output[mask] = i

    return output


def update(frame):
    data = mandelbrot(frame)

    data = np.rot90(data)  # ⟲ 90° против часовой стрелки

    image.set_array(data)
    return [image]


ani = FuncAnimation(fig, update, frames=60, interval=50)
plt.show()
