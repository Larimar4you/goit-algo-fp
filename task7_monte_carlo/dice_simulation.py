import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    """
    Симуляція кидків двох кубиків методом Монте-Карло
    та обчислення ймовірностей сум.
    """
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    probabilities = {total: count / num_rolls for total, count in sums_count.items()}

    return probabilities


analytical = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def plot_probabilities(probabilities, num_rolls):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(8, 5))
    plt.bar(sums, probs)
    plt.xlabel("Сума чисел на кубиках")
    plt.ylabel("Ймовірність")
    plt.title(f"Метод Монте-Карло ({num_rolls} кидків)")
    plt.grid(axis="y")

    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha="center", va="bottom")

    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        probabilities = simulate_dice_rolls(accuracy)

        print(f"\nКількість кидків: {accuracy}")
        print("Порівняння з аналітичними значеннями:")

        for s in range(2, 13):
            print(
                f"{s}: Monte-Carlo={probabilities[s]:.4f}, "
                f"Analytical={analytical[s]:.4f}"
            )

        plot_probabilities(probabilities, accuracy)
