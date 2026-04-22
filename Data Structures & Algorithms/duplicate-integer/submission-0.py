class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_arr={}
        for num in nums:
            if num not in freq_arr:
                freq_arr[num]=1
            else:
                freq_arr[num] += 1
        
        for num in freq_arr:
            if freq_arr[num] > 1:
                return True
        return False
        