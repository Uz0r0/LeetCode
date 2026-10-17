# 202 Happy Number
# Runtime: 4ms
# Memory: 12.23MB

def isHappy(n):
  s = set()
  while n != 1:
    if n in s:
      return False

    s.add(n)

    a = 0
    while n:
      a += (n % 10) ** 2
      n //= 10

    n = a

  return True