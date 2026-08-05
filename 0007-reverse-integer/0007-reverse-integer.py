class Solution:
    def reverse(self, x: int) -> int:
        last = 0
        reverse = 0
        sign = -1 if x<0 else 1
        x = abs(x)

        while x>0:
            last = x%10
            reverse = (reverse*10) + last
            x = x//10
        
        reverse *= sign

        if reverse < -2**31 or reverse > 2**31-1:
            return 0

        return reverse

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna