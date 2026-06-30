
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list.sort(nums);
        i = 0;
        c = 0;
        while (c<len(nums)-1):
            if (nums[c] == nums[c+1]):
                i+=1;    
            c+=1;

        if (i>0):
            return True;
        return False;
