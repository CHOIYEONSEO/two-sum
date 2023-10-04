from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    for i, test in enumerate(nums):
        if target - test in nums[i+1:]:
            return i, nums[i+1:].index(target-test)+(i+1)