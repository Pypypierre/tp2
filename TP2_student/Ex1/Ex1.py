import os
print("The current is", os.getcwd(),"\nIn this directory there is :", os.listdir(),"\nThere is :",os.listdir('test'),"in the ./test/ directory")
os.chdir('test')
os.mkdir('test2')
