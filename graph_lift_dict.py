import matplotlib.pyplot as plt
import numpy as np

from generate_weight import WeightCalculator, pretty_print


def plot_lift_dict(lift_dict, lift_dict2, lift_dict3, lift_dict4, lift_dict5):
    # make data
    x = range(1, len(lift_dict.keys()))
    y = []
    y1 = []
    y2 = [None]
    y3 = []
    y4 = [None, None]
    print(list(lift_dict.keys()))
    for i in range(1, len(lift_dict)):
        for j in lift_dict[i]:
            y.append(j[2])
    for i in range(1, len(lift_dict2)):
        for j in lift_dict2[i]:
            y1.append(j[2])
            y1.append(None)
    for i in range(1, len(lift_dict3)):
        for j in lift_dict3[i]:
            y2.append(j[2])
            y2.append(None)
            y2.append(None)
    for i in range(1, len(lift_dict4)):
        for j in lift_dict4[i]:
            y3.append(j[2])
            y3.append(None)
            y3.append(None)
    for i in range(1, len(lift_dict5)):
        for j in lift_dict5[i]:
            y4.append(j[2])
            y4.append(None)
            y4.append(None)
            


    print(y)
    print(y1)
    print(y2[:-1])
    print(y3)

    # plot
    fig, ax = plt.subplots()

    ax.scatter(x, y)
    ax.scatter(x, y1)
    ax.scatter(x, y2[:-1])
    ax.scatter(x, y3)
    ax.scatter(x, y4[:-2])

    # ax.set(xlim=(0, 8), xticks=np.arange(0, 4),
    #     ylim=(0, 200), yticks=np.arange(0, 200, 10))

    plt.show()

def main():
    calc = WeightCalculator(64, 1.7)

    squat_dict = calc.low_light_rep(12, 'squat')
    bench_dict = calc.low_light_rep(6, 'bench')
    press_dict = calc.low_light_rep(4, 'press')
    clean_dict = calc.low_light_rep(4, 'clean')
    deadlift_dict = calc.low_heavy_rep(4, 'deadlift')
    plot_lift_dict(squat_dict, bench_dict, press_dict, clean_dict, deadlift_dict)

if __name__ == '__main__':
    main()