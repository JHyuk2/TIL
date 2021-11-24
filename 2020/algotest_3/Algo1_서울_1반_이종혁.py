def is_valid(x, y, val):
    # 가로줄에서 같은 숫자가 나오는 경우
    if sudoku_map[x].count(val) > 1:
        return False
    # 세로줄에서 같은 숫자가 나오는 경우
    if transpose_sudoku[y].count(val) > 1:
        return False
    # 3 by 3구역에서 나오는 경우
    sector_x = (x//3) *3
    sector_y = (y//3) *3
    tmp_cnt = 0
    for i in range(sector_x, sector_x+3):
        for j in range(sector_y, sector_y+3):
            if sudoku_map[i][j] == val:
                tmp_cnt += 1
                if tmp_cnt > 1:
                    return False
    # 다 통과한 경우 True
    return True

for tc in range(int(input())):
    lines = int(input())
    sudoku_map = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    input_data = [list(map(int, input().split())) for _ in range(lines)]

    for data in input_data:
        x, y, val = data
        sudoku_map[x][y] = val
        transpose_sudoku = list(map(list, zip(*sudoku_map)))
        if is_valid(x, y, val):
            cnt += 1
        else:
            break
    print(f'#{ tc+1 } { cnt }')

