class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        snum1,snum2,snum3 = str(num1),str(num2),str(num3)
        digits = max(len(snum1),len(snum2),len(snum3))
        snum1 = (digits - len(snum1))*"0"+snum1 if len(snum1)< digits else snum1
        snum2 = (digits - len(snum2))*"0"+snum2 if len(snum2)< digits else snum2
        snum3 = (digits - len(snum3))*"0"+snum3 if len(snum3)< digits else snum3
        key =""
        for i in range(digits):
            key += min(snum1[i],snum2[i],snum3[i])
        return int(key)
        
