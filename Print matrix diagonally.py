from sys import stdin as ip
aa,bb=500,500
def isvalid(i,j,r,c):
    if i<0 or i>=r or j>=c or j<0:
        return False
    else:
        return True
for _ in xrange(int(ip.readline())):
    n,m=map(int,ip.readline().split())
    li=[]
    for i in xrange(n):
        li.append(map(int,ip.readline().split()))
    for k in xrange(n):
        i=k-1
        j=1
        ct=0
        temp=[]
        while isvalid(i,j,n,m):
            temp.append( li[i][j])
            ct+=1
            i-=1
            j+=1
        for i in xrange(ct-1,-1,-1):
            print temp[i],
        print li[k][0],
    for k in xrange(1,m):
        i=n-2
        j=k+1
        ct=0
        temp=[]
        while isvalid(i,j,n,m):
            temp.append( li[i][j])
            i-=1
            j+=1
            ct+=1
        for i in xrange(ct-1,-1,-1):
            print temp[i],
        print li[n-1][k],
