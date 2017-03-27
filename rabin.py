import math
print ("1747 6863 32416185343 32416185371")
def sifrele(text,p=6171054912832631,q=7897466719774591):
    text=toi(text)
    n=p*q
    c=pow(text,2,n)
    return c

def ex_gcd(a,b):
    s=0 ; old_s=1;
    t=1 ; old_t=0;
    r=b ; old_r=a;
    while r :
        bolum = int(old_r / r)
        (old_r,r) = (r, old_r - bolum*r)
        (old_s,s) = (s, old_s - bolum*s)
        (old_t,t) = (t, old_t - bolum*t)
    return (old_s,old_t)

def coz(c,p=6171054912832631,q=7897466719774591):
    mp=pow(int(c),int((p+1)/4),int(p))
    mq=pow(int(c),int((q+1)/4),int(q))
    (yp,yq) =ex_gcd(p,q)
    r1 = (yp*p*mq + yq*q*mp)%(p*q)
    r2 = p*q-r1
    s1 = (yp*p*mq - yq*q*mp)%(p*q)
    s2 = p*q-s1
    print (tos(r1))
    print (tos(r2))
    print (tos(s1))
    print (tos(s2))

def toi(text):
    x=''
    for i in text:
        if ord(i)<100:
            x=x+'0'
            if ord(i)<10:
                x=x+'0'
        x=x+str(ord(i))
    return int(x)

def tos(sayi):
    m=str(sayi)
    y=''
    if len(m)%3 !=0:
        m='0' + m
    for i in range(0,len(m)-2,3):
        y=y + chr (int(m[i] + m[i+1] + m[i+2]))
    return y
        
             




