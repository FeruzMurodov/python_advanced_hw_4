def maximum_of_two(a, b):
    max_number = a if a > b else b
    return max_number


def maximum_of_three(a, b, c):
    max_number = maximum_of_two(maximum_of_two(a, b), maximum_of_two(a, c))
    return max_number


number_a = int(input('Enter number a: '))
number_b = int(input('Enter number b: '))
number_c = int(input('Enter number c: '))
print(maximum_of_three(number_a, number_b, number_c))
