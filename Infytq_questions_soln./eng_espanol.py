def lang_conv(d,l):
    n=[]
    #j=0
    #for j in l:
        #index1=l.index(j)
    for k in d:
        for i in l:
            if k==i:
                n.append(d[k])
    return n

d={"merry":"god","christmas":"jul","hi":"adeous"}
l=["merry","hi","hi"]
print(lang_conv(d,l))