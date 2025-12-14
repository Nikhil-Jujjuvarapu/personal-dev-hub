def lengthOfLongestSubString(s:str)->int:
    charSet = set()
    left, max_length = 0,0
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        max_length = max(max_length,right-left+1)
    return max_length

print(lengthOfLongestSubString('abcabcbb'))