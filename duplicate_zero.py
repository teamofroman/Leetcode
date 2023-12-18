from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
                i += 1

            i += 1


if __name__ == '__main__':
    obj = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    obj.duplicateZeros(arr)

    if arr == [1, 0, 0, 2, 3, 0, 0, 4]:
        print('YES')
    else:
        print('No')
