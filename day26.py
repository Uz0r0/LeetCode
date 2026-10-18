# 242 Valid Anagram
# Runtime: 19ms
# Memory: 13.95MB

def isAnagram(s, t):
  a = dict()
  b = dict()

  if len(s) != len(t):
    return False

  for i in range(len(s)):
    if s[i] in a:
      a[s[i]] += 1
    elif s[i] not in a: 
      a[s[i]] = 1

    if t[i] in b:
      b[t[i]] += 1
    elif t[i] not in b:
      b[t[i]] = 1
                
  return a == b