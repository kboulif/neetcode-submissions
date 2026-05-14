class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1. brute force solution O(n2)
        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return[i,j]
        hashmap = {}
        #2. better complexity (O(n))
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return ([hashmap[comp],i])
            hashmap[num] = i
                
        