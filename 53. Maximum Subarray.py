class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=nums[0]
        current=0
        for i in nums:
            if current<0:
                current=0
            current+=i
            if current>max:
                max=current
        return max
