class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers

        s = s.lower()
        s = s.replace(" ", "")
        print(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        