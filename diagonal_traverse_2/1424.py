class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(list)
        row = len(nums)
        for i in range(row):
            for j in range(len(nums[i])):
                dic[i+j].append(nums[i][j])
        sort_dic = sorted(dic.items(),key=lambda x:x[1])
        ans = []
        for item in dic.items():
            ans.extend(reversed(item[1]))
        return ans