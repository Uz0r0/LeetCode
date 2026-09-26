# 9 Palindrome Number
# Runtime: 20ms
# Memory: 12.22MB

def isPalindrome(x):
  length = len(str(x))
  if x < 0:
    return False
  for i in range(length // 2):
    a = x // (10 ** (length - 1 - i)) % 10
    b = x // (10 ** i) % 10
    if a != b:
      return False

  return True
