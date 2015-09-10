
class Solution(object):
    def twoSum(self, nums, key):
        nums.sort()
        begin = 0
        end = len(nums)-1
        result = []

        while begin < end:
            if nums[begin]+nums[end] == key:
                result.append([nums[begin], nums[end]])
                begin += 1
                end -= 1
            elif nums[begin]+nums[end] < key:
                begin += 1

            else:
                end -= 1
        return result
s = Solution()
print s.twoSum([2,4,1,5,6], 6)