import os
import sys
def main():
    extarr={".go":0,".py":0,".txt":0,".c":0,".pdf":0}
    if len(sys.argv)==3 and os.path.isdir(sys.argv[1]) and sys.argv[2] in extarr:
        for dirName, subdirList, fileList in os.walk(sys.argv[1]):
           for files in fileList:
               name, ext = os.path.splitext(files)
               if ext==sys.argv[2]:
                    print(files)


if __name__ == '__main__':
    main()
