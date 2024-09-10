p=26
g=9
print('the value of p is:%d'%(p))
print('the value of g is:%d'%(g))
a=4
print('the prevate key of a Alaice is:%d'%(a))
x=int(pow(g,a,p))
b=3
print('the prevate key of b Bob is:%d'%(b))
y=int(pow(g,b,p))
ka=int(pow(y,a,p))
kb=int(pow(x,b,p))
print('secret key for Alaice is:%d'%(ka))
print('secret key for Bob is:%d'%(kb))
