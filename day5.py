# 58 Length of Last Word
# Runtime: 0ms
# Memory: 12.49MB

def lengthOfLastWord(s):
        a = s.strip()
        wordList = a.split()
        return len(wordList[-1])