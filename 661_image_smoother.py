from typing import List
from pprint import pprint
from math import floor


class Solution:
    def get_average(
        self, cell_row, cell_col, img: List[List[int]], rows, cols
    ):
        cells_count = 0
        cells_sum = 0

        for i in range(max(0, cell_row - 1), min(rows, cell_row + 2)):
            if i < 0 or i >= rows:
                continue
            for j in range(cell_col - 1, cell_col + 2):
                if j < 0 or j >= cols:
                    continue
                cells_sum += img[i][j]
                cells_count += 1

        if cells_count != 0:
            return floor(cells_sum / cells_count)

        return 0

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])

        new_img = [[0 for j in range(cols)] for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                new_img[row][col] = self.get_average(row, col, img, rows, cols)

        return new_img


if __name__ == '__main__':
    obj = Solution()

    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    res = obj.imageSmoother(img)

    pprint(res)
