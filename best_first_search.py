from copy import deepcopy

def get_heur(current,g):
    c=0
    for i in range(0,len(g)):
        for j in range(0,len(g[0])):
            if (current[i][j]==g[i][j]):
                c+=1
    return c
    
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

def best_find(Q):
    mx=-1
    ind=-1
    for i in range(0,len(Q)):
        if Q[i][1]>mx:
            mx=Q[i][1]
            ind=i
    return ind

def best_first_search(s,g):
    Q=[]
    closed=[]
    Q.append([s,get_heur(s,g)])
    while len(Q)!=0:
        ind=best_find(Q)
        current=Q[ind][0]
        Q.pop(ind)
        closed.append(current)

        if (current==g):
            print("Goal node found")
            print(current)
            break

        else:
            (row,col)=find_blank(current)
            if row!=0:
                new_node=move_up(current)
                print(new_node)
                if new_node not in Q and new_node not in closed:
                    Q.append([new_node,get_heur(new_node,g)])

            if row!=len(s)-1:
                new_node=move_down(current)
                print(new_node)
                if new_node not in Q and new_node not in closed:
                    Q.append([new_node,get_heur(new_node,g)])

            if col!=0:
                new_node=move_left(current)
                print(new_node)
                if new_node not in Q and new_node not in closed:
                    Q.append([new_node,get_heur(new_node,g)])

            if col!=len(s)-1:
                new_node=move_right(current)
                print(new_node)
                if new_node not in Q and new_node not in closed:
                    Q.append([new_node,get_heur(new_node,g)])

            print('\n')


curr_state=[[2,0,3],[1,8,4],[7,6,5]]
goal_state=[[1,2,3],[8,0,4],[7,6,5]]

best_first_search(curr_state,goal_state)