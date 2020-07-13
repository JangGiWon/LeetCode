class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        last = len(nums) - 1
        
        for i in range(0, last):
            current = sorted_nums[i]
            extra = target - current
            
            if extra in sorted_nums[i + 1: last + 1]:
                first_index = nums.index(current)
                second_index = nums.index(extra)
                
                if first_index == second_index:
                    second_index = (first_index + 1) + nums[first_index + 1:].index(extra)
                
                return [first_index, second_index]