from generate_weight import WeightCalculator, pretty_print

y = []
y1 = []
y2 = [None]
y3 = []
y4 = [None, None]

def generate_plan(squat_dict, bench_dict, press_dict, clean_dict, deadlift_dict):
    for i in range(1, len(squat_dict)):
        for j in squat_dict[i]:
            y.append(j[2])
    for i in range(1, len(bench_dict)):
        for j in bench_dict[i]:
            y1.append(j[2])
            y1.append(None)
    for i in range(1, len(press_dict)):
        for j in press_dict[i]:
            y2.append(j[2])
            y2.append(None)
            y2.append(None)
    for i in range(1, len(clean_dict)):
        for j in clean_dict[i]:
            y3.append(j[2])
            y3.append(None)
            y3.append(None)
    for i in range(1, len(deadlift_dict)):
        for j in deadlift_dict[i]:
            y4.append(j[2])
            y4.append(None)
            y4.append(None)

    print(f"Squat: {len(y)} {y}")
    print(f"Bench: {len(y1)} {y1}")
    print(f"Press: {len(y2[:-1])} {y2[:-1]}")
    print(f"Clean: {len(y3)} {y3}")
    print(f"Deadlift: {len(y4[:-2])} {y4[:-2]}")


def main():
    calc = WeightCalculator(64, 1.7)

    squat_dict = calc.low_light_rep(12, 'squat')
    bench_dict = calc.low_light_rep(6, 'bench')
    press_dict = calc.low_light_rep(4, 'press')
    clean_dict = calc.low_light_rep(4, 'clean')
    deadlift_dict = calc.low_heavy_rep(4, 'deadlift')
    generate_plan(squat_dict, bench_dict, press_dict, clean_dict, deadlift_dict)

if __name__ == '__main__':
    main()