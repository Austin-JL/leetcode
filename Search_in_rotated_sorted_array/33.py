class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        low , high = 0 , len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # mid at left ascending
            elif nums[mid] >= nums[low] :
                # target at left ascending
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                # target at right ascending
                else :
                    low = mid + 1
            # mid at rigt ascending
            else:
                # target at right
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                # target at left
                else:
                    high = mid -1 
        return -1