def isValid(s: str) -> bool:
    hash_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    my_queue = []

    for letter in s:
        if letter in hash_map:
            my_queue.append(hash_map[letter])
        else:
            expected = my_queue.pop() if my_queue else ''
            if letter != expected:
                return False 

    if not my_queue:
        return True
    return False