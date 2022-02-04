import csv
df=open('tracesGPS1.csv','r')
dtr=csv.reader(df,delimiter=',')
for row in dtr:
    print(row)
df.close()