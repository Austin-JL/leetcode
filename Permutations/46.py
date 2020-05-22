class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        ans = []
        self.dfs(nums,[],ans)
        return ans
    
    def dfs(self,nums,subset,ans):
        if not nums:
            ans.append(subset)
        for i in range(len(nums)) :
            self.dfs(nums[:i]+nums[i+1:], subset+[nums[i]], ans)
            print(subset)