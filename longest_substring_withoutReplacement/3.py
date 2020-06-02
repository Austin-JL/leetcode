class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = l = 0
        used = {}
        for k,v in enumerate(s):
            if v not in used:
                ans = max(ans,k-l+1)
            else:
                if used[v] < l:
                    ans = max(ans,k-l+1)
                else:
                    l = used[v] + 1
            used[v] = k
        return ans
        