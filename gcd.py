def gcd(a,b):
    r = a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b
if __name__=="__main__":
    print(gcd(1160718174,316258250))