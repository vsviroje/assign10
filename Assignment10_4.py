import os
import sys
import shutil
def main():
    extarr={".go":0,".py":0,".txt":0,".c":0,".pdf":0}
    if len(sys.argv)==4 and os.path.isdir(sys.argv[1]) and not os.path.exists(sys.argv[2]) and sys.argv[3] in extarr:
        path = os.path.abspath(sys.argv[1])
        os.mkdir(sys.argv[2])
        tp = os.path.abspath(sys.argv[2])
        for fileList in os.listdir(sys.argv[1]):
            if fileList.endswith(sys.argv[3]):
                tpath = os.path.join(path, fileList)
                shutil.copy2(tpath, tp)

if __name__ == '__main__':
    main()
