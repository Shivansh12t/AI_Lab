from copy import deepcopy

curr=[['B','C'],['A'],[]]
succ=[]
for i in range(0,len(curr)):
    for j in range(0,len(curr)):
        state=deepcopy(curr)
        if (i!=j and len(state[i])!=0):
            element_removed=state[i].pop(0)
            state[j].insert(0,element_removed)
            succ.append(state)

print(succ)
