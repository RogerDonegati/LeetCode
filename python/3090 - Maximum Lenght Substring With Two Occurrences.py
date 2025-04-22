def maximumLengthSubstring(s: str) -> int:
    result = 0
    hash_map = {}
    left = right = 0

    while right < len(s):
        if s[right] in hash_map:
            hash_map[s[right]] += 1
        else:
            hash_map[s[right]] = 1

        while hash_map[s[right]] >2:
            hash_map[s[left]] -= 1 
            left += 1
        right += 1
        result = max(result, right - left)
    return result