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

def apply_DFS(s,g):
    Q=[]
    closed=[]
    Q.append(s)
    while (len(Q)!=0):
        state=Q.pop(0)
        closed.append(state)
        if (state==g):
            print(state)
            print("Goal Node found")
            break
        
        else:
            (row,col)=find_blank(state)
            succ=[]
            if (row!=0):
                current=move_up(state)
                print(current)
                if current not in Q and current not in closed:
                    succ.append(current)

            if (row!=len(s)-1):
                current=move_down(state)
                print(current)
                if current not in Q and current not in closed:
                    succ.append(current)
            
            if (col!=0):
                current=move_left(state)
                print(current)
                if current not in Q and current not in closed:
                    succ.append(current)
            
            if (col!=len(s[0])-1):
                current=move_right(state)
                print(current)
                if current not in Q and current not in closed:
                    succ.append(current)

            print('\n')
            Q=succ+Q


initial_state=[[1,2,3],[8,0,4],[7,6,5]]
final_state=[[0,1,3],[8,2,4],[7,6,5]]
apply_DFS(initial_state,final_state)