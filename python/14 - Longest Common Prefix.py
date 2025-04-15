def longestCommonPrefix(strs: str) -> str:
    prefix = strs[0]
    for word in strs:
        while word.startswith(prefix) is False and len(prefix) > 0:
            prefix = prefix[:-1]
    return prefix
    