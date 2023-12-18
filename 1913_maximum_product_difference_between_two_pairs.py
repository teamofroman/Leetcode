from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        diff = (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        return diff


if __name__ == '__main__':
    obj = Solution()
    nums = [4, 2, 5, 9, 7, 4, 8]
    print(obj.maxProductDifference(nums))
