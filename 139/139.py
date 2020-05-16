class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp solution
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict :
                    if i + len(word) <= len(s) and s[i:i+len(word)] == word :
                        dp[i+len(word)] = True
        return dp[-1]
        
        