class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        for i in range(rows):
            freq = {}
            for item in board[i]:
                if item in freq and item != ".":
                    return False
                else:
                    freq[item] = 1
            freq2 = {}
            for item in board:
                if item[i] in freq2 and item[i] != ".":
                    return False
                else:
                    freq2[item[i]] = 1

        for i in range(3):
            for j in range(3):
                freq = {}
                for k in range(3):
                    n = board[3*i][3*j + k]
                    l = board[3*i+1][3*j + k]
                    m = board[3*i+2][3*j+ k]

                    if n != "." and n not in freq:
                        freq[n] = 1
                    else:
                        if n != ".":
                            if n in freq: return False
                    if m != "." and m not in freq:
                        freq[m] = 1
                    else:
                        if m != ".":
                            if m in freq: return False
                    if l != "." and l not in freq:
                        freq[l] = 1
                    else:
                        if l != ".":
                            if l in freq: return False

        return True

