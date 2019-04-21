def solve(s):
    b=s.split()
    index=0
    space=[]
    c=[]
    final=""
    for x in range(len(b)):
        var=b[x].capitalize()
        c.append(var)
    for x in range(len(b)):
        spa=0
        str=b[x]
        index+=len(str)
        if index<len(s):
            while s[index]==" ":
                spa+=1
                index+=1
        if spa!=0:
            space.append(spa)
    for x in range(len(c)):
        final+=c[x]
        if x<len(space):
            val=space[x]
            for y in range(val):
                final+=" "
    return final