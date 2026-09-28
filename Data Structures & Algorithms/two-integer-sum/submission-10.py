class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        seen = {}
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             res = [i,j]
        #             break
        # return res
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                res = [seen[diff],i]
                break
            seen[nums[i]]=i
        return res