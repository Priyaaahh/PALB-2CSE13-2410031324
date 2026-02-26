def group_anagrams(strs):
    groups = {}

    for word in strs:
    
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


#Example 1 
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs1))



# Example 2
strs2 = [""]
print(group_anagrams(strs2))



#  Example 3 
strs3 = ["a"]
print(group_anagrams(strs3))
