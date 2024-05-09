import copy
def blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return (i,j)
            
def left(current_state,row,column):
    new_state = copy.deepcopy(current_state)
    new_state[row][column],new_state[row][column-1] = new_state[row][column-1],new_state[row][column]
    return new_state

def right(current_state,row,column):
    new_state = copy.deepcopy(current_state)
    new_state[row][column],new_state[row][column+1] = new_state[row][column+1],new_state[row][column]
    return new_state

def up(current_state,row,column):
    new_state = copy.deepcopy(current_state)
    new_state[row][column],new_state[row-1][column] = new_state[row-1][column],new_state[row][column]
    return new_state

def down(current_state,row,column):
    new_state = copy.deepcopy(current_state)
    new_state[row][column],new_state[row+1][column] = new_state[row+1][column],new_state[row][column]
    return new_state


def heuristic(state,goal):
    val=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=goal[i][j]:
                val=val+1
    return val

def main():

    initial_state = [
        [2,0,3],
        [1,8,4],
        [7,6,5]
    ]
    final_state = [
        [1,2,3],
        [8,0,4],
        [7,6,5]
    ]

    open = []
    closed = []

    open.append([initial_state,heuristic(initial_state,final_state)])

    while(len(open)>0):

        [current_state,heuristic_val] = open.pop(0)

        closed.append(current_state)

        if current_state==final_state:
            print("Found")
            print(closed)
            return True

        (row,column) = blank(current_state)


        if column!=0:
                new_state = left(current_state,row,column)
                if new_state not in open and new_state not in closed:
                    open.append([new_state,heuristic(new_state,final_state)+heuristic(new_state,initial_state)])

        if column!=len(current_state[0])-1:
                new_state = right(current_state,row,column)
                if new_state not in open and new_state not in closed:
                    open.append([new_state,heuristic(new_state,final_state)+heuristic(new_state,initial_state)])

        if row!=0:
                new_state = up(current_state,row,column)
                if new_state not in open and new_state not in closed:
                    open.append([new_state,heuristic(new_state,final_state)+heuristic(new_state,initial_state)])

        if row!=len(current_state)-1:
                new_state = down(current_state,row,column)
                if new_state not in open and new_state not in closed:
                    open.append([new_state,heuristic(new_state,final_state)+heuristic(new_state,initial_state)])

        open = sorted(open , key = lambda x : x[1])

    print("Not found")
    print(closed)

if __name__ == "__main__":
     main()
