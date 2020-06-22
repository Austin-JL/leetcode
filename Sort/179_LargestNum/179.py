class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # practice selection sort
        for i in range(len(nums)):
            pos = i
            for j in range(i+1,len(nums)):
                if self.mycompare(nums[pos],nums[j]):
                    pos = j
            nums[i], nums[pos] = nums[pos], nums[i] 
        return str(int("".join(map(str, nums))))

    # By question, we develope our own sort mechanism   
    def mycompare(self,num1,num2):
        s1 = str(num1)
        s2 = str(num2)
        return s1 + s2 < s2 + s1
    