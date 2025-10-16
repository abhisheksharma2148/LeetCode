class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        t=(0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
        mapping = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
        if month <3:
            year -=1
        
        return mapping[(year+ year//4 - year//100 + year//400 +t[month-1] + day) %7]
