import os
os.chdir('D:\VScode\Code\Python\self_study\peak')
a='_'
c='.py'
d='.txt'
e='.doc'
for s in range(13):
    b=str(s)
    os.rename(a+b+d,a+b+c)