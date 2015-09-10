class Solution():
    def addBinary(self, str1, str2):
        one = int(str1, 2)
        two = int(str2, 2)
        sum = one + two
        sum = bin(sum)

        return sum[2:]

s = Solution()
print s.addBinary("11", "1")