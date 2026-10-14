# 190 Reverse Bits
# Runtime: 19ms
# Memory: 11.90MB

def reverseBits(n):
  ans = 0

  for i in range(31, 0, -1):
    if n:
      if n % 2 == 1:
        ans += (2 ** i)
      n = n // 2
    else:
      break 

  return ans