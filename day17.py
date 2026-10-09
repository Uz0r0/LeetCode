# 125 Valid Palindrome
# Runtime: 16ms
# Memory: 14.93MB

def isPalindrome(s):
  a = [x.lower() for x in s if x.isalnum()]

  for i in range(len(a) // 2):
    if a[i] != a[len(a) - 1 - i]:
      return False

  return True
