import datetime
now_=datetime.datetime(2026,8,6,12,30,45)
tdelt= datetime.timedelta(days=2)
#print(now_.time)
d=datetime.datetime.now()
dt=datetime.datetime.strftime(d,"%B %d,%Y")
#print(dt)
import os
with open("file.txt","r+") as f:
    f.write("what's up?!")
    f.seek(0)
    print(f.tell())
    cont=f.read()
    print(cont)