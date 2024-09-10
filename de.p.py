import math
def gcd(a,h):
    temp=0
    while(1):
        temp=a%h
        if(temp==0):
            return h
        a=h
        h=temp
p=3
q=6
n=p*q
e=p*q
phi=(p-1)*(q-1)
while(e<phi):
    if(gcd(e,phi)==1):
        break
    else:
        e=e+1
k=9
d=(1+(k*phi))/e
msg=13.0
print("message data=",msg)
c=pow(msg,e)
c=math.fmod(c,n)
print("encrypted data=",c)
m=pow(c,d)
m=math.fmod(m,n)
print("orginal mssage sent=",m)
