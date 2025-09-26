class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        open = ""
        for curr in s:
            if curr in ['(','{','[']:
                open += curr
            elif curr in [')','}',']']:
                if not open:
                    return False
                elif curr == mapper[open[-1]]:
                    open = open[:-1]
                else:
                    return False
        if not open:
            return True
        else:
            return False
