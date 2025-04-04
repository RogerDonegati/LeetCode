def lengthOfLastWord(s: str) -> int:        
    result = 0
    s = s.strip()
    for i in range(len(s)-1, -1,-1):
        if s[i] == ' ':
            break
        result += 1
    return result or len(s)

print(lengthOfLastWord('    day'))