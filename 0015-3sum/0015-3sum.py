class Solution:
    def threeSum(self, num: list[int]) -> list[list[int]]:
        res = []
        n = len(num)
        num.sort()
        for i in range(0, n - 2):
            left, right, x = i + 1, n - 1, -1 * num[i]
            if i > 0 and num[i] == num[i - 1]:
                continue
            while left < right:
                if num[left] + num[right] == x:
                    res.append([num[i], num[left], num[right]])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left - 1]:
                        left += 1

                    while left < right and num[right] == num[right + 1]:
                        right -= 1
                elif num[left] + num[right] > x:
                    right -= 1
                else:
                    left += 1

        return res
