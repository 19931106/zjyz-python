class Solution:
    def findRepeatNumber(self, nums) -> int:
        nums.sort()
        print(nums)
        pre = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == pre:
                return pre
            pre = nums[i]

shuzu = [2,3,1,0,2,5,3]
a = Solution()
print(a.findRepeatNumber(shuzu))