print('hello word')
print('童言 10225102509')
for i in range(10):
    print(chr(0x2605),end="")
print(chr(0x2605))
print(chr(0x2605),end="")
print('数据科学与工程导论',end="")
print(chr(0x2605))
for i in range(10):
    print(chr(0x2605),end="")
print(chr(0x2605))
x=int(input())
y=int(input())
z=int(input())
arr=[0,0,0]
arr[0]=x
arr[1]=y
arr[2]=z
arr.sort()
print(arr)
w=int(input())
x=int(input())
y=int(input())
z=int(input())
arr=[0,0,0,0]
arr[0]=w
arr[1]=x
arr[2]=y
arr[3]=z
arr.sort()
arr.reverse()
print(arr)
for i in range(100):
    if i%2!=0 :
        print(i,end="")
        print(" ",end="")
sum=0
for i in range(101):
    sum=sum+i
print(sum)
arr=[1,2,3,4,5]
l=len(arr)
for i in range(l-1,-1,-1):
    print(arr[i],end="")
    print(" ",end="")
s=input()
l=len(s)
flag=0
for i in range(0,l-1):
    if s[i]==s[i+1]:
        print("Yes")
        flag=1
        break
if flag==0:
    print("No")
s=input()
s=s.replace(" ","")
s="".join(s.split())
print(s)
num=int(input())
left=0
right=num
while left<right:
    mid=(left+right)//2
    tmp=mid*mid*mid
    if tmp==num:
        print(mid)
        import sys
        sys.exit()
    elif tmp>num:
        right=mid-1
    else:
        left=mid+1
if left*left*left>num:
    print(left-1)
else:
    print(left)
sum=1
n=int(input())
for i in range(1,n+1):
    sum=sum*i
print(sum)