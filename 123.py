
year = int(input("請輸入年份："))
if((year %4 == 0 and year %100 != 0) or (year % 400 == 0)):
    run = True
else:
    run = False     #這行也可以不用寫
i = 1900
sum = 0
while i < year - 1:
    i += 1
    if((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):
        sum += 366
    else: 
        sum += 365
month = int(input("請輸入月份："))
j = 1
while j < month:
    if((j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12)):
        sum += 31
    elif j == 2:
        if run:
            sum += 29
        else: 
            sum += 28
    else: sum += 30
    j += 1
week = (sum + 1) % 7
if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
    day = 31
elif month == 2:               #二月的巢狀判斷，閏年二月29，平年28
    if run:
        day = 29
    else:
        day = 28
else:
    day = 30
print("日\t一\t二\t三\t四\t五\t六")
count = 0    #定義一個計數器，以便後面的換行
k = 0
while k <= week:   #每個月的開始第一週前面的空格數
    k += 1
    print("\t",end="")
    count += 1
    if (count % 7 == 0):
        print("\n")
   # count=7 進行換行
p = 1
while p <= day:    #顯示天數
    print(p,"\t",end="")     #列印  table 不換行
    p += 1
    count += 1
    if(count % 7 == 0):
        print("\n")        #count=7 進行換行