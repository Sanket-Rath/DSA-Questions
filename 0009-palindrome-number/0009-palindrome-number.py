class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        last = 0
        reverse = 0
        n = x

        while n>0:
            last = n%10
            reverse = (reverse*10) + last
            n = n//10

        if reverse == x:
            return True
        else:
            return False   


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna