"""
偶数：打印 number // 2 并返回
奇数：打印 3*number + 1 返回
"""


def collatz(num):
    if num % 2 == 0:
        result = num // 2
        print(result)
    elif num % 2 == 1:
        result = (3 * num) + 1
        print(result)
    return result


if __name__ == '__main__':
    print('Enter number:')
    try:
        number = int(input())
        while number != 1:
            number = collatz(number)
    except BaseException as error:
        print('Oops! Must input integer number\n', format(error))
