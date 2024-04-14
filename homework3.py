def print_sum(x, y):
    index = 0
    large_value = max(x, y)
    small_value = min(x, y)
    sum = 0
    while small_value <= large_value:
        sum += small_value
        small_value += 1
    print(sum)


case_cnt = int(input())
while case_cnt > 0:
    x, y = input().split()

    print_sum(int(x), int(y))

    case_cnt -= 1