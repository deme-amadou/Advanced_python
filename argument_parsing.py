import sys
import getopt

print(sys.argv[0])

FILENAME = sys.argv[1]
MESSAGE = sys.argv[2]
with open(FILENAME, "a+") as f: 
    f.write(MESSAGE + "\n")

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename","message"])
print(f"Opts : {opts} ")
print(f"Args : {args} ")