import csv
l=[]
df=open('tracesGPS2.csv','r')
dtr=csv.reader(df,delimiter=',')
for row in dtr:
    #print(row)
    l.append(row)

df.close()
print(l[0],l[-1])
print("The difference of latitude",float(l[-1][0])-float(l[1][0]))