class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict=dict()

        for i in range(len(nums)):
            numdict[nums[i]]=i

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in numdict.keys() and numdict.get(diff)!=i:
                return [i,numdict.get(diff)]


        