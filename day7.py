# 2544 Alternating Digit Sum
# Runtime: 0ms
# Memory: 12.32MB

def alternateDigitSum(n):
  digits = [int(d) for d in str(n)]
  c = True
  ans = 0

  for num in digits:
    ans += num if c else -num
    c = not c
            
  return ans
        