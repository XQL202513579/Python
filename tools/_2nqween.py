def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 初始化
    count = 0
    black_positions = [-1] * n
    # 检查黑皇后放置是否合法
    def is_black_valid(row, col):
        if board[row][col] == 0:  # 障碍位置
            return False
        for i in range(row):
            # 检查列冲突
            if black_positions[i] == col:
                return False
            # 检查主对角线冲突（左上到右下）
            if black_positions[i] - i == col - row:
                return False
            # 检查副对角线冲突（右上到左下）
            if black_positions[i] + i == col + row:
                return False
        return True
    # 检查白皇后放置是否合法
    def is_white_valid(white_positions, row, col):
        if board[row][col] == 0:  # 障碍位置
            return False
        if black_positions[row] == col:  # 位置已被黑皇后占用
            return False
        for i in range(row):
            if white_positions[i] == col:  # 列冲突
                return False
            if white_positions[i] - i == col - row:  # 主对角线冲突
                return False
            if white_positions[i] + i == col + row:  # 副对角线冲突
                return False
        return True
    # 放置白皇后（回溯）
    def place_white(row, white_positions):
        nonlocal count
        if row == n:  # 所有白皇后放置完成
            count += 1
            return
        for col in range(n):
            if is_white_valid(white_positions, row, col):
                white_positions[row] = col
                place_white(row + 1, white_positions)
                white_positions[row] = -1
    # 放置黑皇后（回溯）
    def place_black(row):
        if row == n:  # 所有黑皇后放置完成，开始放置白皇后
            white_positions = [-1] * n
            place_white(0, white_positions)
            return
        for col in range(n):
            if is_black_valid(row, col):
                black_positions[row] = col
                place_black(row + 1)
                black_positions[row] = -1
    # 开始放置黑皇后
    place_black(0)
    print(count)
if __name__ == "__main__":
    solve()