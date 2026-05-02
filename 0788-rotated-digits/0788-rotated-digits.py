class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_same = {'0', '1', '8'}
        valid_diff = {'2', '5', '6', '9'}
        count = 0
        for i in range(1, n + 1):
            num = str(i)
            is_valid = True
            is_good = False
            for digit in num:
                if digit in valid_same:
                    continue
                elif digit in valid_diff:
                    is_good = True
                else:
                    is_valid = False
                    break
            if is_valid and is_good:
                count += 1
        return count