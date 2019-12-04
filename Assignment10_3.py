import os
import sys
import shutil
def main():
    if len(sys.argv)==3 and os.path.isdir(sys.argv[1]) and not os.path.exists(sys.argv[2]):
        path = os.path.abspath(sys.argv[1])
        os.mkdir(sys.argv[2])
        tp=os.path.abspath(sys.argv[2])
        for fileList in os.listdir(sys.argv[1]):
            tpath=os.path.join(path,fileList)
            shutil.copy2(tpath,tp)

if __name__ == '__main__':
    main()
