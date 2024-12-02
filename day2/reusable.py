from itertools import combinations
from textwrap import dedent


def get_numbers_from_line(line):
    return list(map(int, line.split()))


def get_consecutive_pairs(iterable):
    return zip(iterable, iterable[1:])


def progression_check(iterable, condition):
    for a, b in get_consecutive_pairs(iterable):
        if condition(a, b):
            return False
    return True


def has_difference(a, b):
    return 0 < abs(a - b) <= 3


def is_increasing(a, b):
    return a >= b or not has_difference(a, b)


def is_decreasing(a, b):
    return a <= b or not has_difference(a, b)


def is_safe(iterable):
    result = progression_check(iterable, is_increasing)
    if not result:
        result = progression_check(iterable, is_decreasing)
    return result


def is_safe_v2(iterable):
    return is_safe(iterable) or any(
        is_safe(it) for it in combinations(iterable, len(iterable) - 1)
    )


def get_small_data():
    data = dedent(
        """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
    ).strip()
    return data.splitlines()
