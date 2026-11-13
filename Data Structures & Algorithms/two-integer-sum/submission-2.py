class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            second_target = target - nums[i]
            if second_target in nums_dict.keys():
                return [nums_dict[second_target], i]
            nums_dict[nums[i]] = i

        