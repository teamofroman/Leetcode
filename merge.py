from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        id1 = 0
        id2 = 0

        while id2 < n:
            if nums2[id2] <= nums1[id1]:
                nums1.insert(id1, nums2[id2])
                nums1.pop()
                id2 += 1
                m += 1
            elif nums1[id1] == 0 and id1 >= m:
                nums1[id1] = nums2[id2]
                id2 += 1
            id1 += 1


if __name__ == '__main__':
    obj = Solution()

    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    res_array = [1, 2, 2, 3, 5, 6]

    obj.merge(nums1, m, nums2, n)
    assert nums1 == res_array

    # Example 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    res_array = [1]

    obj.merge(nums1, m, nums2, n)
    assert nums1 == res_array

    # Example 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    res_array = [1]

    obj.merge(nums1, m, nums2, n)
    assert nums1 == res_array

    # Example 4
    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m = 6
    nums2 = [1, 2, 2]
    n = 3
    res_array = [-1, 0, 0, 1, 2, 2, 3, 3, 3]

    obj.merge(nums1, m, nums2, n)
    assert nums1 == res_array

    # Example 5
    nums1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    m = 5
    nums2 = [-1, -1, 0, 0, 1, 2]
    n = 6
    res_array = [-1, -1, -1, 0, 0, 0, 0, 0, 1, 2, 3]

    obj.merge(nums1, m, nums2, n)
    assert nums1 == res_array
