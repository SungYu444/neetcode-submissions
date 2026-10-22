class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        temp = {}   
        for i in strs: 
            word = i.strip()
            total = []
            for j in word:
                total.append(ord(j))
            key = tuple(sorted(total))
            if key not in temp:
                temp[key] = []
            temp[key].append(i)
        return list(temp.values())