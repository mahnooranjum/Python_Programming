# -*- coding: utf-8 -*-


import subprocess 
 
n = 100
c = 10
linker = ""
cmd = "ab -l -n " + str(n) + " -c " + str(c) + " -k -g "+ "n" + str(n) +"c" + str(c) + ".gp " + linker
# cmd = "ab -l -n " + str(n) + " -c " + str(c) + " -k -g " + linker
r = subprocess.check_output(cmd, shell=True, universal_newlines=True)
print(r)

