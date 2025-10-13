class Solution:
    def dayOfYear(self, date: str) -> int:
        month_to_day = {0:0,1:31,2:28,3:31,4:30,
                        5:31,6:30,7:31,8:31,
                        9:30,10:31,11:30,12:31}
        date_list=date.split('-')
        year, month,day = int(date_list[0]), int(date_list[1]), int(date_list[2])
        no_of_days = 0
        for i in range(month):
            no_of_days += month_to_day[i]
        no_of_days += day
        if month > 2:
            if year%400==0:
                no_of_days +=1
            elif year%4==0 and year%100!=0:
                no_of_days +=1
        return no_of_days
