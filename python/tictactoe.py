class Solution:
    def tictactoe(self, moves) -> str:
        rows, columns = [0] * 3, [0] * 3
        dg1, dg2 = 0, 0
        for k, (i, j) in enumerate(moves):
            value = 1 if k % 2 == 0 else -1
            rows[i] += value
            columns[j] += value
            if i == j:
                dg1 += value
            if 2 - j == i:
                dg2 += value
            for x in (rows[i], columns[j], dg1, dg2):
                if x == 3 * value:
                    return 'A' if k % 2 == 0 else 'B'
        return 'Pending' if len(moves) < 9 else 'Draw'



solution = Solution()
solution.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])