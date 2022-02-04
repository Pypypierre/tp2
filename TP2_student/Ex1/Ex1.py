import os
import shutil
print("The current is", os.getcwd(),"\nIn this directory there is :", os.listdir(),"\nThere is :",os.listdir('test'),"in the ./test/ directory")
shutil.move('IPSA.txt','test')
os.mkdir('test2')
