from typing import List
from pprint import pprint
from math import floor


class Solution:
    def get_average(
        self, cell_row, cell_col, img: List[List[int]], rows, cols
    ):
        cells_count = 0
        cells_sum = 0

        for i in range(cell_row - 1, cell_row + 2):
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

        new_img = []
        for row in range(rows):
            new_row = []
            for col in range(cols):
                ave = self.get_average(row, col, img, rows, cols)
                new_row.append(ave)
            new_img.append(new_row)

        return new_img


if __name__ == '__main__':
    obj = Solution()

    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    res = obj.imageSmoother(img)

    pprint(res)
