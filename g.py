import math
def gcd(e,h):
    temp=a%h
    if(temp==0):
        return h
        a=h
        h=temp
p=2
q=9
n=p*q
e=9
phi=(p-1)*(q-1)
while(e<phi):
    if(gcd(e,phi)==1):
        break
    else:
        e=e+1
k=9
d=(1+(k*phi))/e
msg=20.0
print("message data=",msg)
c=pow(msg,e)
c=math.fmod(c,d)
print("encrypted data=",c)
m=pow(c,d)
m=math.fmod(m,n)
print("original message sent=",m)
