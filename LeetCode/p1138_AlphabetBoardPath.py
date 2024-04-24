# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

class Solution(object):
    def alphabetBoardPath(self, target):
        i = 0
        j = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz' # ideally can be already populated static dictionary for O(1) access
        result = ""
        for character in target:
            index = alphabet.index(character)
            newI = index % 5
            newJ = int(index / 5)
            diffI = newI - i
            diffJ = j - newJ
            extraDown = False
            if diffJ >= 0:
                result += "U"*diffJ
            else:
                if newJ == 5: # To handle if moving down to z, cannot move past imaginary places
                    diffJ += 1
                    extraDown = True
                result += "D"*(-1*diffJ)

            if diffI >= 0:
                result += "R"*diffI
            else:
                result += "L"*(-1*diffI)

            if extraDown:
                result += "D"

            result += "!"
            i = newI
            j = newJ

        return result
    
if __name__ == "__main__":
    print(Solution().alphabetBoardPath("zdz"))