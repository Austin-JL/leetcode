class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        slow , cur = 1,0
        ans = []
        while slow < len(nums)+1:
            if slow == len(nums) or nums[slow] - nums[slow-1] != 1:
                if slow -1 != cur:
                    ans.append(str(nums[cur]) + "->" + str(nums[slow-1]))
                else: ans.append(str(nums[slow-1]))
                cur = slow
            slow += 1
        return ans