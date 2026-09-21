class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counts(words: str):
            count = {}
            for letter in words:
                if letter in count:
                    count[letter] += 1
                else:
                    count[letter] = 1
            return count

        count_s = counts(s)
        count_t = counts(t)
        if count_s == count_t:
            return True
        return False
        