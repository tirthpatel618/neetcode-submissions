class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        # can do a 2 pointer approach
        # you require nums[i] = nums[k] - nums[j]
        # i.e -nums[i] = nums[k] + nums[j]
        length = len(nums)
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            left = i + 1
            right = length - 1
            target = -n
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res


