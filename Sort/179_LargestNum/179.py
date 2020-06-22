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
        # return str(int("".join(map(str, nums))))
        
        # practice insertion sort  
        for i in range(1,len(nums)):
            val = nums[i]
            j = i -1
            while j >= 0 and not self.mycompare(val,nums[j]):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = val
        # return str(int("".join(map(str, nums))))



        #practice bubble sort
        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                #if self.mycompare(nums[j],nums[j+]):
                if self.mycompare(nums[j],nums[j+1]):
                    nums[j+1],nums[j] = nums[j],nums[j+1]
        # return str(int("".join(map(str, nums))))

        
        #quick sort
        self.quicksort(nums, 0, len(nums)-1)

        #comnbine number to string
        return str(int("".join(map(str, nums))))

    # By question, we develope our own sort mechanism   
    def mycompare(self,num1,num2):
        s1 = str(num1)
        s2 = str(num2)
        return s1 + s2 < s2 + s1
    

    def quicksort(self, nums, l,r):
        if l < r:
            pi = self.partition(nums,l,r)
            self.quicksort(nums,l,pi-1)
            self.quicksort(nums,pi+1,r)
    
    def partition(self,nums,l,r):
        i = l - 1
        pivot = nums[r]
        for j in range(l,r):
            if not self.mycompare(nums[j],pivot):
                i = i+1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1], nums[r] = nums[r],nums[i+1]
        return i+1
    