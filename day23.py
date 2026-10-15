# 2220 Minimum Bit Flips to Convert Number
# Runtime: 0ms
# Memory: 12.29MB

def minBitFlips(start, goal):
  xor_val = start ^ goal
  ans = 0

  while xor_val > 0:
    ans += xor_val & 1 
    xor_val >>= 1  
        
  return ans