# 217 Contains duplicate 
# Runtime: 26ms
# Memory: 25.80MB

def containsDuplicate(nums):
  a = set()

  for i in nums:
    if i not in a:
      a.add(i)
    else:
      return True
    
  return False