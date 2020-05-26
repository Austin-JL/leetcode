class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key =lambda x: x[0])
        for i in intervals:
            if not ans:
                ans.append(i)
            elif ans[-1][-1] < i[0]:
                ans.append(i)
            else:
                ans[-1][-1] = max(i[-1], ans[-1][-1])
        return ans