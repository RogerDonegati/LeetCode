def romanToInt(s: str) -> int:
    hash_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    result = 0
    previous_val = 0
    for letter in s[::-1]:
        if previous_val > hash_map[letter]:
            result -= hash_map[letter]
        else:
            result += hash_map[letter]
        previous_val = hash_map[letter]

    return result