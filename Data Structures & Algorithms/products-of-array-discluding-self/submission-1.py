
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        
        zero_count = nums.count(0)
        total_product_without_zero = 1
        
        for num in nums:
            if num != 0:
                total_product_without_zero *= num
                
        for num in nums:
            if zero_count > 1:
                ans.append(0)
            elif zero_count == 1:
                if num == 0:
                    ans.append(total_product_without_zero)
                else:
                    ans.append(0)
            else:
                ans.append(total_product_without_zero // num)
                
        return ans
