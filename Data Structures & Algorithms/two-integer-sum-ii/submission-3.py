class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            TSum=numbers[l]+numbers[r]
            if TSum > target:
                r-=1
            elif TSum < target:
                l+=1
            else:
                return [l+1,r+1]
        return []