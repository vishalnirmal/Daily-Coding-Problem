def filetype(file):
    return '.' in file
def find_longest(string):
    lines = string.split('\n')
    files = [i.split('\t') for i in lines]
    maxn = 0
    maxf = 0
    for i in range(len(files)):
        if filetype(files[i][-1]) and maxn < len(files[i]):
            maxn = len(files[i])
            maxf = i
    path = files[maxf][-1]
    maxn-=1
    for i in range(maxf-1, -1, -1):
        if len(files[i]) == maxn:
            path = files[i][-1]+'/'+path
            maxn-=1
    print(path)
if __name__ == "__main__":
    string = "dir\n\tsubdir1\n\t\tfile2.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile1.ext" 
    string = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    find_longest(string)