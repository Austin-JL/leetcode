class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        count = collections.Counter({0:1})
        for n in nums:
            temp = collections.Counter()
            for val in count:
                temp[val+n] += count[val]
                temp[val-n] += count[val]
            count = temp
        return count[S]