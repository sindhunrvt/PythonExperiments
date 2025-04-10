from collections import Counter


class Solution:
    def checkanagram(self, s, t):
        Counter_s = Counter(s)
        Counter_t = Counter(t)
        return Counter_s == Counter_t

s1 = Solution()
print(s1.checkanagram("rat", "car"))
print(s1.checkanagram("anagram", "nagaram"))