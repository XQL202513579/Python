import os
import shutil
a='D:\VScode\Code\python\where'
os.chdir(a)
for f in os.listdir(a):
    b=os.path.join(a,f)
    input(f'是否删除{b}')
    try:
        if os.path.isfile(f) or os.path.islink(f):
            os.remove(f)
        elif os.path.isdir(f):
            shutil.rmtree(f)
    except Exception as c:
        print(c)