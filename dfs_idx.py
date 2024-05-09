from copy import deepcopy

def find_blank(s):
    for i in range(0,len(s)):
        for j in range (0,len(s[0])):
            if s[i][j]==0:
                return (i,j)
            
def move_left(s):
    (i,j)=find_blank(s)
    state=deepcopy(s)
    state[i][j],state[i][j-1]=state[i][j-1],state[i][j]
    return state

def move_right(s):
    (i,j)=find_blank(s)
    state=deepcopy(s)
    state[i][j],state[i][j+1]=state[i][j+1],state[i][j]
    return state

def move_up(s):
    (i,j)=find_blank(s)
    state=deepcopy(s)
    state[i][j],state[i-1][j]=state[i-1][j],state[i][j]
    return state

def move_down(s):
    (i,j)=find_blank(s)
    state=deepcopy(s)
    state[i][j],state[i+1][j]=state[i+1][j],state[i][j]
    return state

def depth_limited_search(s,g,l_depth):
    Q=[]
    closed=[]
    Q.append([s,0])
    while len(Q)!=0:
        current_state,depth=Q.pop(0)
        closed.append(current_state)
        if current_state==g:
            print("Goal node found")
            print(s)
            break
        else:
            if depth<l_depth:
                (row,col)=find_blank(current_state)
                succ=[]

                if row!=0:
                    new_state=move_up(current_state)
                    print(new_state)
                    if new_state not in Q and new_state not in closed:
                        succ.append([new_state,depth+1])

                if row!=len(s)-1:
                    new_state=move_down(current_state)
                    print(new_state)
                    if new_state not in Q and new_state not in closed:
                        succ.append([new_state,depth+1])

                if col!=0:
                    new_state=move_left(current_state)
                    print(new_state)
                    if new_state not in Q and new_state not in closed:
                        succ.append([new_state,depth+1])

                if col!=len(s[0])-1:
                    new_state=move_up(current_state)
                    print(new_state)
                    if new_state not in Q and new_state not in closed:
                        succ.append([new_state,depth+1])
                print()
                Q=succ+Q


initial_state=[[1,2,3],[8,0,4],[7,6,5]]
final_state=[[0,1,3],[8,2,4],[7,6,5]]
depth_limited_search(initial_state,final_state,2)

