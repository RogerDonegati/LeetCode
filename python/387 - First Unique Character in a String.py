def firstUniqChar(s: str) -> int: 
    hash_map = {}

    for i, letter in enumerate(s):
        if letter in hash_map:
            hash_map[letter][1] += 1
        else:
            hash_map[letter] = [i, 1]

    for key, values in hash_map.items():
        if values[1] == 1:
            return values[0]
    
    return -1