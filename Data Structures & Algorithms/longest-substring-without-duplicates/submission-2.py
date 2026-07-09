class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()
        maxLen = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            length = r - l + 1
            maxLen = max(maxLen, length)
            r += 1
        return maxLen


