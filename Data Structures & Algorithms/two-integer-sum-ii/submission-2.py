class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in range(len(numbers)):
            compliment=target-numbers[i]
            if hashmap[compliment]:
                return [hashmap[compliment],i+1]
            hashmap[numbers[i]]=i+1
        return []