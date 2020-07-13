class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31:
            return 0
        if x < 0:
            rev = int('-' + str(-x)[::-1])
        else:
            rev = int(str(x)[::-1])
        if rev < -2**31 or rev > 2**31:
            rev = 0
        return rev