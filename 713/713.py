class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int] 
        :type k: int
        :rtype: int
        """
        
        # window sliding & two pointers 
        prod = 1
        ans = 0
        left = 0 
        
        #[10,5,2,6]
        for right in range(len(nums)):
            prod *= nums[right]
            print (prod)
            while left <= right and prod >= k :
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans 
            
                
                