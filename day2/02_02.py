from day2 import DATA_PATH, read_line_by_line

from .reusable import get_numbers_from_line, get_small_data, is_safe_v2


def solution(data):
    count = 0
    # data = get_small_data()
    for line in data:
        report = get_numbers_from_line(line)
        if is_safe_v2(report):
            count += 1
    return count


def main():
    data = read_line_by_line(DATA_PATH, skip_empty=True, strip=True)
    result = solution(data)
    print(result)


if __name__ == "__main__":
    main()
