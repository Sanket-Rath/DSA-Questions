class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_map = dict()

        for i in range(0,len(nums)):
            hash_map[nums[i]] = 0
        
        j=0
        for k in hash_map:
            nums[j] = k
            j += 1
        
        return j

    
        



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna