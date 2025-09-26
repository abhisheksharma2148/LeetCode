class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        valid_sub = {
            'I': ['V','X'],
            'X': ['L','C'],
            'C': ['D','M']
        }

        num = 0
        prev = None

        for i in s:
            if prev in valid_sub and i in valid_sub[prev]:
                num = num - 2*(roman_dict[prev]) + roman_dict[i]    
            else:
                num = num + roman_dict[i]
            prev = i

        return num
        
