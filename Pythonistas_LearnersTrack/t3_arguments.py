import sys 
import getopt


opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

print(opts)
print(args)

for opt, arg in opts:
    print(opt)
    print(arg)

'''
args = sys.argv
print(*args)

'''


