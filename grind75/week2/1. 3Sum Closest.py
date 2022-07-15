class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        supp = float('inf')
        nums.sort()
        # target too small
        current = sum(nums[:target])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-target:])
        if current <= target:
            return current

        for index, n in enumerate(nums):
            if n == nums[index - 1] and index > 0:
                continue
            else:
                left = index + 1
                right = len(nums) - 1
                while left < right:
                    if n > target:
                        if res == 0:
                            return nums[0] + nums[1] + nums[2]
                        return res
                    current = n + nums[left] + nums[right]
                    if current == target:
                        return current
                    tmp = abs(current - target)
                    if tmp <= supp:
                        supp = tmp
                        res = current

                    if current > target:
                        right -= 1
                    else:
                        left += 1
        return res