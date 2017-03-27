import math

def sprseri(sayi,b=2):
    fark=sayi
    a=0
    while fark:
        while b**(a+1) <= fark:
            a=a+1
        fark=fark - b**a
        print (b,"^",a,"=",b**a)
        a=0
