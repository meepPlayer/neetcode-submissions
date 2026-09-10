class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            index = i + 1
            while index != len(nums):
                if nums[i] + nums[index] == target: 
                    return [i, index]
                index += 1