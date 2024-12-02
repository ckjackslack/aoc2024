from day1 import DATA_PATH, read_line_by_line


def solution(data):
    left_nums, right_nums = [], []

    for line in data:
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)

    occurences = []
    for left in left_nums:
        occurences.append(right_nums.count(left))

    sum_of_distances = 0
    for l, r in zip(left_nums, occurences):
        distance = l * r
        sum_of_distances += distance

    return sum_of_distances


def main():
    data = read_line_by_line(DATA_PATH, skip_empty=True, strip=True)
    result = solution(data)
    print(result)


if __name__ == "__main__":
    main()
