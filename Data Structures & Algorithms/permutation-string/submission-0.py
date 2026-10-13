class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {chr(i + ord('a')): 0 for i in range(26)}
        s2Count = {chr(i + ord('a')): 0 for i in range(26)}

        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1

        matches = 0
        for c in s1Count:
            if s1Count[c] == s2Count[c]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add the right character
            char = s2[r]
            s2Count[char] += 1

            if s1Count[char] == s2Count[char]:
                matches += 1
            elif s1Count[char] + 1 == s2Count[char]:
                matches -= 1

            # Remove the left character
            char = s2[l]
            s2Count[char] -= 1

            if s1Count[char] == s2Count[char]:
                matches += 1
            elif s1Count[char] - 1 == s2Count[char]:
                matches -= 1

            l += 1

        return matches == 26
        