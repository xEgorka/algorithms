# https://leetcode.com/problems/flipping-an-image

# Flip and invert by rows using two pointers. Don't invert second time


from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            left, right = 0, len(image[i]) - 1
            while left <= right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                image[i][left] = 0 if image[i][left] else 1
                if right != left:
                    image[i][right] = 0 if image[i][right] else 1
                left += 1
                right -= 1
        return image


def main() -> int:
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(Solution().flipAndInvertImage(image))
    return 0


if __name__ == '__main__':
    main()
