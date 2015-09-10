class Solution():
    def threeSum(self, nums, key):
        result =[]
        for each in nums:
            ret = self.twoSum(nums, key, each)
            if len(ret) > 0:
                result.append(ret)
        return result

    def twoSum(self, nums, key, each):
        nums.sort()
        begin = 0
        end = len(nums)-1
        result = []

        while begin < end:
            if nums[begin]+nums[end] == key-each:
                result = [nums[begin], nums[end], each]
                begin += 1
                end -= 1
            elif nums[begin]+nums[end] < key:
                begin += 1

            else:
                end -= 1

        return result

s = Solution()
print s.threeSum([1, 2, 5, 3, 4], 8)