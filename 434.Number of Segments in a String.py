class Solution:
    def countSegments(self, s: str) -> int:
        s_list= s.split(' ')
        s_length = 0
        for i in s_list:
            if i!="":
                s_length +=1
        return s_length
