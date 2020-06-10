class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        row,col = len(mat),len(mat[0])
        for i in range(row):
            for j in range(col):
                dic.setdefault(i-j,[]).append(mat[i][j])
        for key,val in dic.items():
            val.sort(reverse=True)
        for i in range(row):
            for j in range(col):
                mat[i][j] = dic[i-j].pop()
        return mat