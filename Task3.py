def reverse_sum_reverse(a: str, b: str):
    def reverse_number(num: str):
        result = ''
        for i in range(len(num)):
            required_index = len(num) - 1 - i
            result = result + num[required_index]
        return result

    number_a = int(reverse_number(a))
    number_b = int(reverse_number(b))
    print(number_a, number_b)
    return int(reverse_number(str(number_a + number_b)))


n = input('Enter the first number: ')
k = input('Enter the second number: ')
print(reverse_sum_reverse(n, k))
