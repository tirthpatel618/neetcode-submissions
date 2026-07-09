class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # value -> index

        # brute force - check every number combination
        # two pass - make the hash, then use it
        # one pass - both in one go
        for i in range(len(nums)):
            diff = target - nums[i]
        # search if the number needed for nums[i] + diff = target is in hash
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i 



