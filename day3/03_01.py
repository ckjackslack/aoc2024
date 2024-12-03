import re

from day3 import DATA_PATH, read_line_by_line

from .reusable import MUL_PATTERN


def solution(data):
    total = 0
    for line in data:
        matches = re.findall(MUL_PATTERN, line)
        for match in matches:
            a, b = map(int, match)
            total += a * b
    return total


def main():
    data = read_line_by_line(DATA_PATH, skip_empty=True, strip=True)
    result = solution(data)
    print(result)


if __name__ == "__main__":
    main()
