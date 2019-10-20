def isYearLeap(year):
    comun=year%4
    if(comun>0):
        return False
    elif(comun==0):
        comun=year%100
        if(comun==0):
            comun=year%400
            if(comun==0):
                return True
            elif(comun>0):
                return False
        elif(comun>0):
            return True
def daysInMonth(year,month):
    if(month==1 or month==3 or month==5 or month==7 or month==9):
        return 31
    elif(month==4 or  month==6 or month==8 or month==10 or month==11 or month==12):
        return 30
    else:
        if(isYearLeap(year)):
            return 29
        else:
            return 28
testYears=[1900,2000,2016,1987]
testMonths=[2,2,1,11]
testResults=[28,29,31,30]
for i in range(len(testYears)):
    yr=testYears[i]
    mo=testMonths[i]
    print(yr,mo,"->",end="")
    result=daysInMonth(yr,mo)
    if result==testResults[i]:
        print("OK")
    else:
        print("Failed")
