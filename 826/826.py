class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        tot = 0
        
        # make tuple of (difficulty,profit)
        x = zip(difficulty,profit)
        x.sort()
        
        # pos : store position in x
        # temp: store temp profit
        
        pos = 0
        temp = 0
        for ability in sorted(worker):
            while pos < len(x):
                # tuple : (10.20)
                if(ability >= x[pos][0]):
                    temp  = max(temp,x[pos][1])
                    pos += 1
                else:
                    break
                    
            tot += temp
            
        return tot
        