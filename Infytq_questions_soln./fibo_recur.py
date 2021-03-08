import time
def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m]=memo(m-1,d)+memo(m-2,d)
        return d[m]

d={0:1,1:1}
print(memo(48,d))
