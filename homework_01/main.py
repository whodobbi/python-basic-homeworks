"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]
    # return list(map(lambda x: x ** 2, numbers)) - можно было и так, но для такой задачи не факт, что нужно


print(power_numbers(1, 2, 5, 7))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    return [num for num in nums if (filter_type == ODD and num % 2 != 0) or
                                    (filter_type == EVEN and num % 2 == 0) or
                                    (filter_type == PRIME and is_prime(num))]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(filter_numbers([1, 2, 3], "odd"))
print(filter_numbers([2, 3, 4, 5], "even"))
print(filter_numbers([2, 3], "prime"))
