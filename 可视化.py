#读取文件第一行
import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename="forme.csv"
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
 
#一列一列读取表格中数据
    dates,opens,highs,lows,closes,adjcloses=[],[],[],[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%m/%d/%Y")
        dates.append(current_date)
        a=float(row[1])
        opens.append(a)
        b=float(row[2])
        highs.append(b)
        d=float(row[3])
        lows.append(d)
        e=float(row[4])
        closes.append(e)
        g=float(row[6])
        adjcloses.append(g)

#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,opens,c='orange',label="open")#label与legend()来标注每种数据的折线颜色
plt.plot(dates,highs,c='green',label="high")
plt.plot(dates,lows,c='yellow',label="low")
plt.plot(dates,closes,c='black',label="close")
plt.plot(dates,adjcloses,c='purple',label="adj close")

plt.xlabel("Date",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("",fontsize=16)
plt.tick_params (axis="both",which="major",labelsize=16)
plt.legend(loc='center left', bbox_to_anchor=(0.12, 1.12),ncol=5)#ncol=5 5个标识 行排列


plt.show()


    
    
