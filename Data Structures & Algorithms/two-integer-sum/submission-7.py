class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums: array of ints 
        # target: target int
        # i+j == target
        #list.sort(nums)

        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if (nums[i]+nums[j]==target):
                    answer = [i,j]
                    if i!=j:
                        return answer
                j+=1
            i+=1
        