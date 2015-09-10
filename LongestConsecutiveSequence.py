from collections import OrderedDict


class Solution(object):
    def longestConsecutiveSeq(self, num):
        seqDic = OrderedDict()

        for each in num:
            seqDic[each] = each

        maxlength = 0

        for key in num:
            left = key - 1
            right = key + 1
            cnt = 1

            while left in seqDic:
                cnt += 1
                seqDic.pop(left)
                left -= 1

            while right in seqDic:
                cnt += 1
                seqDic.pop(right)
                right += 1

            if cnt > maxlength:
                maxlength = cnt

        return maxlength

s = Solution()
print s.longestConsecutiveSeq([1, 2, 3, 4, 5,6,7,8,199, 99, 100])
