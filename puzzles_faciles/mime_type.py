import sys
import math

DEBUG = True

def debug(*kwargs):
    if DEBUG:
        print(*kwargs, file=sys.stderr)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mime = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()

    debug(ext,mt)

    mime[ext.lower()] = mt

debug("mime",mime)

for i in range(q):
    fname = input()  # One file name per line.
    
    debug("fname", fname)
    
    extension = ""

    if fname.count(".") == 0 :
        extension = "NON EXISTANT"
    else :
        extensions = fname.split(".")
        leng = len(extensions)
        debug("leng", leng)
        extension = extensions[leng - 1]
        debug("extension", extension)

    if extension.lower() in mime.keys():
        print(mime[extension.lower()])
    elif extension == "NON EXISTANT":
        print("UNKNOWN")
    else:
        print("UNKNOWN")
