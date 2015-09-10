from itertools import permutations


class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)

        cnt = 1
        for each in permutations(nums, length):
            if cnt == 2:
                return each
            cnt += 1

s = Solution()
print s.nextPermutation([1,2,3])