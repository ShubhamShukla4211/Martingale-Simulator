import matplotlib.pyplot as plt

def plot_sample_paths(martingales, n=10):
    plt.figure(figsize=(10, 6))
    for i in range(n):
        plt.plot(martingales[i], alpha=0.7)
    plt.xlabel("Step")
    plt.ylabel("Martingale Value")
    plt.title("Sample Martingale Paths (Bounded Random Walk)")
    plt.grid(True)
    plt.show()

def plot_final_histogram(martingales):
    final_values = martingales[:, -1]
    plt.figure(figsize=(8, 5))
    plt.hist(final_values, bins=30, edgecolor='k', alpha=0.7)
    plt.xlabel("Limiting Value")
    plt.ylabel("Frequency")
    plt.title("Distribution of Limiting Values of Martingale Paths")
    plt.grid(True)
    plt.show()