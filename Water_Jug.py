from collections import defaultdict
J1, J2, T = 4,3,2 

visited = defaultdict(lambda:False) 

print("steps :")

def WJ(amt1, amt2):
    if (T in (amt1,amt2)):
        print(amt1,amt2)
        print('Found')
        return True
    if visited[(amt1,amt2)] == False:
        print(amt1,amt2)
        visited[(amt1,amt2)] = True
    
    else:
        return False
    return (WJ(0,amt2) or WJ(amt1,0) or WJ(J1,amt2) or WJ(amt1,J2) or WJ(amt1+min(amt2,J1-amt1),amt2-min(amt2,J1-amt1)) or WJ(amt1-min(amt1,J2-amt2),amt2+min(amt1,J2-amt2)))


WJ(0,0)
