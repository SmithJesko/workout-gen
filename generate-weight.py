# Copyright (C) 2022 Smith Jesko <https://smithjesko.com>
# This program is free software: you can redistribute it and/or modify

def pretty_print(lift_dict):
    print(str(lift_dict[0][0]).upper() + '\n')
    for i in range(1, len(lift_dict)):
        print('Set ' + str(i) + ':')
        for j in lift_dict[i]:
            print('Warmup: ' + str(j[0]) + 'x' + str(j[1]))
            print('Working: ' + str(j[2]) + 'x' + str(j[3]) + '\n')

class WeightCalculator:
        def __init__(self, weight, height):
            self.weight = weight # kg
            self.height = height # m

            self.starting_squat = 115
            self.starting_bench = 95
            self.starting_press = 0
            self.starting_deadlift = 0
            self.starting_clean = 0

            self.smallest_weight_increase = 5
            self.largest_weight_increase = 15
            self.smallest_reps = 5
            self.largest_reps = 12

            self.warmup_reps = 8
            self.warmup_percent = 0.7

        def BMI(self):
            # < 18.5 = underweight
            # 18.5 - 24.9 = normal
            # 25 - 29.9 = overweight
            # 30 - 34.9 = obese
            # 35 - 39.9 = severely obese
            # > 40 = morbidly obese
            return self.weight / (self.height * self.height) # BMI = kg/m2

        def low_light_rep(self, sets, lift):
            if lift == 'squat':
                starting_weight = self.starting_squat
            elif lift == 'bench':
                starting_weight = self.starting_bench
            elif lift == 'press':
                starting_weight = self.starting_press
            # elif lift == 'deadlift':
            #     starting_weight = self.starting_deadlift
            # elif lift == 'clean':
            #     starting_weight = self.starting_clean
            else:
                print('Invalid lift')
                return

            lift_dict = {}
            lift_dict[0] = [lift]
            for i in range(1, sets+1):
                counter = i
                lift_dict[counter] = []
                lift = starting_weight + (self.smallest_weight_increase * i)
                warmup = int(lift * self.warmup_percent)
                lift_dict[counter].append([warmup, self.warmup_reps, lift, self.smallest_reps])
            return lift_dict

        def low_heavy_rep(self, sets, lift):
            if lift == 'clean':
                starting_weight = self.starting_squat
            else:
                print('Invalid lift')
                return

            lift_dict = {}
            lift_dict[0] = [lift]
            for i in range(1, sets+1):
                counter = i
                lift_dict[counter] = []
                lift = starting_weight + (self.largest_weight_increase * i)
                warmup = int(lift * self.warmup_percent)
                lift_dict[counter].append([warmup, self.warmup_reps, lift, self.smallest_reps])
            return lift_dict


def main():
    calc = WeightCalculator(64, 1.7)
    print('BMI: ' + str(calc.BMI()) + '\n')

    # print(calc.low_rep(3, 'squat'))
    # print(calc.low_rep(3, 'bench'))
    pretty_print(calc.low_light_rep(3, 'bench'))
    pretty_print(calc.low_heavy_rep(3, 'clean'))

if __name__ == '__main__':
    main()
