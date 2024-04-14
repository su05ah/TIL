def print_diamond(size):
    index = size // 2

    # size만큼 줄반복
    for i in range(size):
        # size만큼 문자 찍기
        char = 0
        while char < size :
            # 시작할때 - 기호 찍기
            if char >= index and char <= size - index - 1:
                print("+", end="")
            else:
                print("*", end="")
            char += 1

        # 줄바꿈 수정
        print("")

        # 인덱스 조정
        if i < size // 2:
            index -= 1
        else:
            index += 1

case_cnt = int(input())
while case_cnt > 0:
    diamond_size = int(input())
    print_diamond(diamond_size)
    case_cnt -= 1