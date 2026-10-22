class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for word in strs:
            key = "".join(sorted(word))   # "act" and "cat" both become "act"
            if key not in temp:
                temp[key] = []
            temp[key].append(word)
        return list(temp.values())