import re

from day3 import DATA_PATH, read_line_by_line

from .reusable import DO_PATTERN, DONT_PATTERN, MUL_PATTERN

ANY_PATTERN = rf"({DO_PATTERN}|{DONT_PATTERN}|{MUL_PATTERN})"


def solution(data):
    _apply = True
    total = 0
    for line in data:
        matches = re.findall(ANY_PATTERN, line)
        for match in matches:
            whole, a, b = match

            if "don't" in whole:
                _apply = False
                continue
            elif "do" in whole:
                _apply = True
                continue

            if "mul" in whole:
                a, b = int(a), int(b)
                if _apply:
                    total += a * b
    return total


def main():
    data = read_line_by_line(DATA_PATH, skip_empty=True, strip=True)
    result = solution(data)
    print(result)


if __name__ == "__main__":
    main()
