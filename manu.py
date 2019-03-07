def biggest(a,b,c):
    if a>=b and a>=c :
        return(a)
    elif b>=a and b>=c:
     return(b)
    else:
        return(c)    
d=biggest(2,8,9)
print(d)
