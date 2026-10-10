# 69 Sqrt(x)
# Runtime: 1157ms
# Memory: 12.45MB

def mySqrt(x):
  i = 0

  while i * i <= x:
    i += 1

  return i - 1
