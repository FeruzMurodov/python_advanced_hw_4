def sum_digits(entered_value: str) -> int:
    result = sum(map(lambda x: int(x), entered_value))
    return result


def find_max_digit(entered_value: str) -> int:
    result = max(map(lambda x: int(x), entered_value))
    return result


def find_min_digit(entered_value: str) -> int:
    result = min(map(lambda x: int(x), entered_value))
    return result


while True:
    value = input('Enter integer or type "x" to exit: ')
    if value.isdecimal():
        command = input('Type function "max", "min" or "sum"  ')
        if command == 'sum':
            print(sum_digits(value))
        elif command == 'max':
            print(find_max_digit(value))
        elif command == 'min':
            print(find_min_digit(value))
        else:
            print('Incorrect command has been typed!')
    elif value == 'x':
        break
    else:
        print('Incorrect value entered: ')
print('Thank you for using our calculator!')
