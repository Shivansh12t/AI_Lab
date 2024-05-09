from copy import deepcopy

def get_heur(current,g):
    c=0
    for i in range(0,len(g)):
        for j in range(0,len(g[0])):
            if (current[i][j]!=0):
                if (current[i][j]!=g[i][j]):
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
    mx=100
    ind=-1
    for i in range(0,len(Q)):
        if Q[i][1]<mx:
            mx=Q[i][1]
            ind=i
    return ind

def simple_hill(s, g):
    current=s
    while (True):
        if (current==g):
            print("Goal node found")
            print(current)
            break
        else:
            (row,col)=find_blank(current)
            succ=[]
            if (row!=0):
                new_node1=move_up(current)
                heur1=get_heur(new_node1,g)
                succ.append([new_node1,heur1])

            if (row!=len(s)-1):
                new_node2=move_down(current)
                heur2=get_heur(new_node2,g)
                succ.append([new_node2,heur2])

            if (col!=0):
                new_node3=move_left(current)
                heur3=get_heur(new_node3,g)
                succ.append([new_node3,heur3])

            if (col!=len(s[0])-1):
                new_node4=move_right(current)
                heur4=get_heur(new_node4,g)
                succ.append([new_node4,heur4])

            ind=best_find(succ)
            print(succ)
            print(succ[ind][0],'\n')

            if (get_heur(current,g)==succ[ind][1]):
                print("Local maxima reached")
                break

            current=succ[ind][0]
            




curr_state=[[2,0,3],[1,8,4],[7,6,5]]
goal_state=[[1,2,3],[8,0,4],[7,6,5]]

simple_hill(curr_state,goal_state)


            

            

