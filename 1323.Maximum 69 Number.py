class Solution:
    def maximum69Number (self, num: int) -> int:
        maxval= num
        for i in range(len(str(num))):
            temp = str(num)
            if temp[i] =='6':
                temp = temp[0:i] + '9' + temp[i+1:]
            maxval = max(maxval,int(temp))
        return maxval
