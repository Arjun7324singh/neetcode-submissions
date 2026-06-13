class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set() 
        n = len(nums)
        
        for i in range(n):
            seen = set() 
            
            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])
                
                if complement in seen:
                    res.add(tuple(sorted([nums[i], nums[j], complement])))
                
                seen.add(nums[j])
                
        return [list(triplet) for triplet in res]
