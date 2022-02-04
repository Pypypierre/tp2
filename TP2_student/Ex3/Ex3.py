l=[]
i=0
f=open("MontyPython_TheGalaxySong.txt","r")
lines=f.readlines()
for a in lines:
    if "miles" in a :
        l.append(a)
        i+=1
print(l,"\nThere is ",i,"line where there is the word 'miles'")
f.close()
f1= open("out.txt", "a")
for b in l:
    f1.write(b)
f1.close()
