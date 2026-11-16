class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}
        for i,num in enumerate(nums):
            compliment=target-num
            if compliment in hashset:
                return [hashset[compliment],i]
            hashset[num]=i