class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums))
        temp.sort()
        
        for i, v in enumerate(temp):
            nums[i] = v
        
        return len(temp)