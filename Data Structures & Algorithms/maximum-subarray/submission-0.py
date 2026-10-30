class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mn = max(nums)
        start = nums.index(mn)
        ans = mn
        cur = 0
        for x in nums[start:]:
            cur += x
            if ans < cur:
                ans = cur
        cur = ans
        if start > 0:
            for x in reversed(nums[0:start]):
                cur += x
                if ans < cur:
                    ans = cur
        return ans