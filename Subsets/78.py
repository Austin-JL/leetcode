class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums :
            ans += [i + [n] for i in ans]
        return ans