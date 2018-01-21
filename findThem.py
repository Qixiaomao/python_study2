import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1 and os.path.exists(sys.argv[1]):
        themAll = []
        for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
            for filename in filenames:
                if os.path.splitext(filename)[1] == '.txt':
                    themAll.append(os.path.join(dirpath, filename))
            print (themAll)
    else:
        print ("Please input like this:./findThem.py/home/f10w")
