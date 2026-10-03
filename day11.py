# 14 Longest Common Prefix
# Runtime: 0ms
# Memory: 19.16MB

def longestCommonPrefix(strs):
  for i in range(len(strs[0])):
    for str in strs:
      if i == len(str) or str[i] != strs[0][i]:
        return strs[0][:i]
     
  return strs[0]