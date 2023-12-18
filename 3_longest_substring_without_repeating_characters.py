class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = 0
        end = 1

        max_len = 0

        if len(s) <= 1:
            return len(s)

        while end < len(s):
            try:
                id = s.index(s[end], begin, end)
            except ValueError:
                id = -1

            if id != -1:
                max_len = max(max_len, end - begin)
                begin = id + 1

            end += 1

        max_len = max(max_len, end - begin)
        return max_len


if __name__ == '__main__':
    s = 'dvdf'
    obj = Solution()
    print(obj.lengthOfLongestSubstring(s))
