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
testData=[1900,2000,2016,1987,2100,2400]
testResults=[False,True,True,False,False,True]
for i in range(len(testData)):
    yr=testData[i]
    print(yr,"->",end="")
    result=isYearLeap(yr)
    if result==testResults[i]:
        print("OK")
    else:
        print("Failed")
