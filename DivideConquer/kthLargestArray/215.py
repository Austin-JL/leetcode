class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def fastSelect(nums,k):
            pivot = int(uniform(0, len(nums)))
            l = []
            r = []
            for key,val in enumerate(nums):
                if val < nums[pivot] and key != pivot:
                    l.append(val)
                elif key != pivot:
                    r.append(val)
                    
            if k -1 == len(l):
                return nums[pivot]
            elif k <= len(l):
                return fastSelect(l,k)
            else:
                return fastSelect(r,k-len(l)-1)
        return fastSelect(nums,len(nums)-k+1)
                
                