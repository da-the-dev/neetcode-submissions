class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(list(filter(lambda c: c in "abcdefghijklmnopqrstuvwxyz0123456789", list(s.lower()))))
        return ss == "".join(list(reversed(ss)))