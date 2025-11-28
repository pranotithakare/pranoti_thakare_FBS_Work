# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.
def generatePalindromeNo():
    num = 0
    while True:
        temp = num
        rev = 0
        # Reverse the number mathematically
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        if rev == num:
            yield num
        num += 1

gen = generatePalindromeNo()
for _ in range(20):
    print(next(gen), end=' ')
