from martingale import generate_martingales
from plotter import plot_sample_paths, plot_final_histogram

if __name__ == "__main__":
    martingales = generate_martingales()
    plot_sample_paths(martingales)
    plot_final_histogram(martingales)