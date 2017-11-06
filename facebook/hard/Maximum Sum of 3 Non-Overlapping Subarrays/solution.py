class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 3*k:
            return []
           
        partial = [0]*(len(nums) - k + 1)#partial solutions starting from index i of length k
        
        partial[0] = sum(nums[:k])#first sum of the inital k numbers
        
        for i in range(1,len(nums) - k + 1):
            partial[i] = partial[i-1] + nums[i + k -1] - nums[i-1]#calculate the rest of the sums
        
        dp = [[0,0]] *len(partial), [[0,0]] *len(partial) 
        dp_front_max, dp_back_max = -sys.maxint, -sys.maxint #maintain the max value going back and front
            
        for i in range(len(partial)):
            if(partial[i] > dp_front_max):#for every partial sum find the max
                dp[0][i] = [partial[i],i]#maintain the range of the max value
                dp_front_max = partial[i]
            else:
                dp[0][i] = dp[0][i-1]#unless the max is already found
                
        for i in range(len(partial) - 1, -1, -1):
            if(partial[i] > dp_back_max):#for every partial sum going backwards
                dp[1][i] = [partial[i],i]#main the range of the max value
                dp_back_max = partial[i]
            else:
                dp[1][i] = dp[1][i+1]#unless the value is already found

        
        ret, maxval = [], -sys.maxint#find the maximum interval
        for i in range(k, len(partial) - k):
            if partial[i] + dp[0][i - k][0] + dp[1][i + k][0] > maxval:
                ret = dp[0][i - k][1] , i,  dp[1][i + k][1]#returns 3 intervals for which the maxmimum interval exist
                maxval = partial[i] + dp[0][i - k][0] + dp[1][i + k][0]#get the max value for the middle interval
        return ret
        
        
