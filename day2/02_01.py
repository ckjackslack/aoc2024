from day2 import DATA_PATH, read_line_by_line

from .reusable import get_numbers_from_line, is_safe


def solution(data):
    count = 0
    for line in data:
        report = get_numbers_from_line(line)
        if is_safe(report):
            count += 1
    return count


def main():
    data = read_line_by_line(DATA_PATH, skip_empty=True, strip=True)
    result = solution(data)
    print(result)


if __name__ == "__main__":
    main()
