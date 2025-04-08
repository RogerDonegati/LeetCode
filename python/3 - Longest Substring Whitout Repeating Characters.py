def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    result = 0
    currentChars = {}
    while i  < len(s):
        if s[i] not in currentChars:
            currentChars[s[i]] = i
        else:
            result = max(result, len(currentChars))
            i = currentChars[s[i]]
            currentChars = {}
        i += 1

    result = max(result, len(currentChars))
    return result