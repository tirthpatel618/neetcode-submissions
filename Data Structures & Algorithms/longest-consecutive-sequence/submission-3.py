class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # starting candidates are those who are not +1 to the one before it
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

        # naive approach
        for num in nums:
            length = 1
            while (num + length) in numSet:
                lenth += 1
            longest = max(longest, length)


        