from sortedcontainers import SortedList


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = SortedList(s)
        t1 = SortedList(t)

        return s1 == t1


if __name__ == '__main__':
    obj = Solution()
    print(obj.isAnagram("anagram", "nagaram"))
