class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        # built count dict
        for n in nums:
            if n not in count:
                count[n] = 1
            else :
                count[n] += 1
        
        # using bucket sort 
        
        bucket = {}
        
        for val,freq in count.items():
            if freq not in bucket:
                bucket[freq] = [val]
            else:
                bucket[freq].append(val)
                
        ans = []
        for x in range(len(nums), 0, -1):
            if x in bucket:                
                for i in bucket[x]:
                    ans.append(i)
        return ans[:k]