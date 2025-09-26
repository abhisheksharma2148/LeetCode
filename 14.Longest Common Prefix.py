class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp =""
        max_iterations = min(len(word) for word in strs)
        no_of_words = len(strs)
        for letter_idx in range(max_iterations):
            temp = ""
            for word_idx in range(no_of_words):
                if temp == "":
                    temp = strs[word_idx][letter_idx]
                elif temp == strs[word_idx][letter_idx]:
                    continue
                else:
                    return lcp
            lcp += temp
        return lcp
        
