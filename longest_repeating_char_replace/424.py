class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = l = 0
        count = Counter()
        maxf = -1
        for i,v in enumerate(s):
            count[v] += 1
            maxf = max(maxf,count[v])
            if i - l + 1 - maxf > k:
                count[s[l]] -=1
                l += 1
                
            ans = max(ans,i-l+1)
        return ans