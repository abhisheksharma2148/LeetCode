class Solution:
    def reverseVowels(self, s: str) -> str:
        t = list(s)
        vowels = set('aeiouAEIOU')
        left, right = 0, len(t)-1
        while left < right:
            if t[left] not in vowels:
                left +=1
            elif t[right] not in vowels:
                right -=1
            else:
                t[left], t[right] = t[right], t[left]
                left +=1
                right -=1
        return ''.join(t)

        
