import matplotlib.pyplot as plt

def plot_cumulative(returns):
    cumulative = (1 + returns).cumprod()
    plt.figure(figsize=(10,5))
    plt.plot(cumulative)
    plt.title("Cumulative Return")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.show()

