class Solution:
    def maxCrossing(self,nums,mid):
        # initial max to be infinity small
        max_L = max_R = float("-inf")
        # using sum to store temporary sum:
        sum = 0 
        for i in range(mid-1, -1, -1):
            sum += nums[i]
            max_L = max(sum,max_L)
        sum = 0
        for i in range(mid, len(nums)):
            sum += nums[i]
            max_R = max(sum,max_R)
        return max_R + max_L
    
    def maxSubArray(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        mid = len(nums)//2
        L = self.maxSubArray(nums[:mid])
        R = self.maxSubArray(nums[mid:])
        C = self.maxCrossing(nums,mid)
        return max(L,R,C)