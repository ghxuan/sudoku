from copy import deepcopy
from random import shuffle, choice


class SudoKu:
    def __init__(self):
        self.chessboard, self.base_set, self.empty = [], set(range(1, 10)), set()
        self.blocks, self.base_list, self.solutions = [deepcopy(self.base_set) for _ in range(9)], range(9), 0

    def board(self, n):
        # 列，行，块
        rows, cols, blocks = deepcopy(self.blocks), deepcopy(self.blocks), deepcopy(self.blocks)
        chessboard = [[0 for _ in range(9)] for _ in range(9)]
        self.dfs(rows, cols, blocks, chessboard, 0, 0)
        end_board = deepcopy(chessboard)
        while len(self.empty) < n:
            i, j = choice(self.base_list), choice(self.base_list)
            if (i, j) not in self.empty:
                self.check_unique(rows, cols, blocks, chessboard, i, j)
        return end_board, chessboard, rows, cols, blocks

    # 生成数独，不过是解数独而已，只不过解的是空的数独
    def dfs(self, rows, cols, blocks, chessboard, i, j):
        if i == 9:
            return True
        if j == 9:
            return self.dfs(rows, cols, blocks, chessboard, i + 1, 0)
        if chessboard[i][j] == 0:
            r = i // 3 * 3 + j // 3
            optionals = list(rows[j] & cols[i] & blocks[r])
            shuffle(optionals)
            for opt in optionals:
                chessboard[i][j] = opt
                rows[j].remove(opt)
                cols[i].remove(opt)
                blocks[r].remove(opt)
                if self.dfs(rows, cols, blocks, chessboard, i, j + 1):
                    return True
                chessboard[i][j] = 0
                rows[j].add(opt)
                cols[i].add(opt)
                blocks[r].add(opt)
        else:
            return self.dfs(rows, cols, blocks, chessboard, i, j + 1)
        return False

    # 挖洞 i,j 位置，判断是否有唯一解
    def check_unique(self, rows, cols, blocks, chessboard, i, j):
        cur = chessboard[i][j]
        r = i // 3 * 3 + j // 3
        chessboard[i][j] = 0
        rows[j].add(cur)
        cols[i].add(cur)
        blocks[r].add(cur)
        self.unique_solution(deepcopy(rows), deepcopy(cols), deepcopy(blocks), deepcopy(chessboard), 0, 0)
        if self.solutions == 1:
            self.empty.add((i, j))
            return False
        else:
            chessboard[i][j] = cur
            rows[j].remove(cur)
            cols[i].remove(cur)
            blocks[r].remove(cur)
            return True

    # 判断是否有唯一解
    def unique_solution(self, rows, cols, blocks, chessboard, i, j):
        if i == 0 and j == 0:
            self.solutions = 0
        if i == 9:
            self.solutions += 1
            return False
        if j == 9:
            return self.unique_solution(rows, cols, blocks, chessboard, i + 1, 0)
        if chessboard[i][j] == 0:
            r = i // 3 * 3 + j // 3
            optionals = list(rows[j] & cols[i] & blocks[r])
            for opt in optionals:
                chessboard[i][j] = opt
                rows[j].remove(opt)
                cols[i].remove(opt)
                blocks[r].remove(opt)
                if self.unique_solution(rows, cols, blocks, chessboard, i, j + 1):
                    return True
                chessboard[i][j] = 0
                rows[j].add(opt)
                cols[i].add(opt)
                blocks[r].add(opt)
        else:
            return self.unique_solution(rows, cols, blocks, chessboard, i, j + 1)


if __name__ == '__main__':
    s = SudoKu()
    for sudo in s.board(50):
        print(sudo)
