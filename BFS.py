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

def apply_BFS(s,g):
    Q=[]
    closed=[]
    Q.append(s)
    while (len(Q)!=0):
        current=Q.pop(0)
        closed.append(current)
        if (current==g):
            print(current)
            print("Goal node found")
            break
        else:
            (row,col)=find_blank(current)
            if (row!=0):
                new_node=move_up(current)
                print(new_node)
                if new_node not in closed and new_node not in Q:
                    Q.append(new_node)

            if (row!=len(s)-1):
                new_node=move_down(current)
                print(new_node)
                if new_node not in closed and new_node not in Q:
                    Q.append(new_node)

            if (col!=0):
                new_node=move_left(current)
                print(new_node)
                if new_node not in closed and new_node not in Q:
                    Q.append(new_node)

            if (col!=len(s[0])-1):
                new_node=move_right(current)
                print(new_node)
                if new_node not in closed and new_node not in Q:
                    Q.append(new_node)

            print('\n')


    





initial_state=[[1,2,3],[8,0,4],[7,6,5]]
final_state=[[2,8,1],[0,4,3],[7,6,5]]
apply_BFS(initial_state,final_state)

