def pal_check(inp1):
    #String1=inp1
    #i=0
    Strin1=inp1.upper()
    rev=''.join(reversed(Strin1))
    if Strin1==rev:
        return True
    else:
        return False

print(pal_check("Civic"))