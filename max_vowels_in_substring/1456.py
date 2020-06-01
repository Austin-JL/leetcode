class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ["a","e","i","o","u"]
        ans = window_count = 0
        for i, v in  enumerate(s):
            if i >= k :
                if s[i-k] in vowel:
                    window_count -= 1
            if s[i] in vowel:
                window_count += 1
            ans = max(ans,window_count)
        return ans
        