class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for l in s:
            seen[l] = seen.get(l, 0) + 1

        for l in t:
            seen[l] = seen.get(l, 0) - 1

        for l in seen.values():
            if l != 0:
                return False

        return True


        