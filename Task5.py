def calculate_danger(depth: int):
    rate_of_danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    return rate_of_danger


def find_safe_depth(max_danger: float):
    depth_min = 0
    depth_max = 4
    depth_middle = (depth_min + depth_max) / 2
    middle_danger = calculate_danger(depth_middle)
    while abs(middle_danger) > max_danger:
        if middle_danger > 0:
            depth_min = depth_middle
        else:
            depth_max = depth_middle
        depth_middle = (depth_min + depth_max) / 2
        middle_danger = calculate_danger(depth_middle)
    return depth_middle


def main():
    required_rate_of_danger = float(input('Enter the rate of danger: '))
    if required_rate_of_danger < 0:
        print('You have entered impossible rate of danger! Try again.')
    else:
        print(f'Approximately depth of safety placing: {find_safe_depth(required_rate_of_danger):.9f} metres')

main()