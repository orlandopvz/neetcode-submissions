class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0]*26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            signature = tuple(count)
            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]
        return list(groups.values())