class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        numset= set(nums)
        ansnum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    nev = -(nums[i] + nums [j])
                    if nev in numset and nums.index(nev) != i and nums.index(nev) != j and sorted([nums[i], nums[j], nev]) not in ans:
                        ans.append(sorted([nums[i], nums[j], nev]))
                        ansnum += 1
        return ans