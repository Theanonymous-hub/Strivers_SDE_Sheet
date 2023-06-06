class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left =0
        right=len(nums)-1
        check_point=0
        while check_point<=right:
            if nums[check_point]==0:
                nums[check_point],nums[left]=nums[left],nums[check_point]
                left+=1
                check_point+=1
            elif nums[check_point]==2:
                nums[check_point],nums[right]=nums[right],nums[check_point]
                right-=1
            else:
                check_point+=1
