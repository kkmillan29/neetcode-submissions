class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsmap = dict()
        for i in range(len(nums)):
            if numsmap.get(nums[i]):
                return True
            numsmap[nums[i]]=True

        return False
        