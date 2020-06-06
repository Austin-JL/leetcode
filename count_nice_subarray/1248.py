class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, cur_sum = 0, 0
        sum_dict = {0:1}
        for num in nums:
            cur_sum += num & 1
            if cur_sum - k in sum_dict:
                res += sum_dict[cur_sum - k]
            sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1
        return res