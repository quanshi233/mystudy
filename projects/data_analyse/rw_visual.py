import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi=128)
    point_numbers = range(rw.number_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    ax.get_xaxis().set_visible(1)
    ax.get_yaxis().set_visible(1)
    plt.show()
    keep_running = input("quit? (y/n) :")
    if keep_running == 'y':
        break