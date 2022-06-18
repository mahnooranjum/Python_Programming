


import os 


file = './d8_KDE_3var.py'
folder = './../Misc/'

path = folder

fsize = 0
if os.path.isfile(path):
    fsize = os.path.getsize(file)
elif os.path.isdir(path):
    fsize = sum(d.stat().st_size for d in os.scandir(folder) if d.is_file())
else:
    print("[ERR] Invalid Path")

print(fsize)

# print(sum(d.stat().st_size for d in os.scandir(folder) if d.is_file()))