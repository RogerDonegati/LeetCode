def reverseWords(s: str) -> str:  
    result = ''
    left = 0
    right = 0
    while right < len(s):
        if s[right] == ' ':
            result += s[left:right][::-1] + ' '
            left = right + 1
        right += 1

    result += s[left:right][::-1]
    return result