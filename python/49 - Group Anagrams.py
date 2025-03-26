def groupAnagrams(strs: list[str]) -> list[list[str]]:
    results = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key in results:
            results[key].append(word)
        else:
            results[key] = [word]
    return list(results.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]
