# 66 Plus One
# Runtime: 0ms
# Memory: 12.36MB

def plusOne(self, digits):
  wholeNum = int(''.join(map(str, digits)))
  wholeNum += 1
  
  preResult = list(str(wholeNum))

  result = list(map(int, preResult))    

  return result
        