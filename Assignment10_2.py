import os
import sys
def main():
    extarr={".go":0,".py":0,".txt":0,".c":0,".pdf":0}
    if len(sys.argv)==4 and os.path.isdir(sys.argv[1]) and sys.argv[2] in extarr and sys.argv[3] in extarr:
        path = os.path.abspath(sys.argv[1])
        for fileList in os.listdir(sys.argv[1]):
            if fileList.endswith(sys.argv[2]):
                tpath=os.path.join(path,fileList)
                base = os.path.splitext(fileList)[0]
                os.rename(tpath,base + sys.argv[3])

if __name__ == '__main__':
    main()
