iterator=0

def one_point_cross(chromo1,chromo2):
    index=len(chromo1)//2
    chromo1[index:],chromo2[index:]=chromo2[index:],chromo1[:index]

def mutation(chromo1):
    global iterator
    index=[3,2,1,0]
    pos=iterator%4
    x=index[pos]
    chromo1[x]=abs(1-chromo1[x])
    iterator+=1

def get_value(W,V,chromo,Weight_of_bag):
    weigh=0
    value=0
    for i in range (0,len(chromo)):
        if chromo[i]==1:
            weigh+=W[i]
            value+=V[i]

    if (weigh>Weight_of_bag):
        return 0
    else:
        return value

def find_best(current_population,W,V,Weight_of_bag):
    index=0
    current_best=current_population[0]
    current_val=get_value(W,V,current_best,Weight_of_bag)
    for i in range(1,len(current_population)):
        if (current_val<get_value(W,V,current_population[i],Weight_of_bag)):
            current_best=current_population[i]
            current_val=get_value(current_population[i],W,V,Weight_of_bag)
            index=i

    current_population.pop(index)

    return current_best


def genetic_algo(current_population,W,V,Weight_of_bag):
    first=find_best(current_population,W,V,Weight_of_bag)
    second=find_best(current_population,W,V,Weight_of_bag)
    third=find_best(current_population,W,V,Weight_of_bag)
    fourth=find_best(current_population,W,V,Weight_of_bag)  
    current_population.append(first)
    current_population.append(second)
    current_population.append(third)
    current_population.append(fourth)
    one_point_cross(current_population[2],current_population[3])
    mutation(current_population[3])
    print("Current Population:",current_population)


W=[45,40,50,90]
V=[3,5,8,10]

current_population=[[1,1,1,1],
                    [1,0,0,0],
                    [1,0,1,0],
                    [1,0,0,1]]

for _ in range(0,10):
    genetic_algo(current_population,W,V,100)

print("\nFittest chromosome",current_population[0])

    









