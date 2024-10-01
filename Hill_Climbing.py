import copy



# h1=number of tiles displaced from their destined position.
def h1(start_state,goal_state):
    ans=0
    for i in range(0,3):
        for j in range(0,3):
            if(start_state[i][j]!='B' and start_state[i][j]!=goal_state[i][j]):
                ans+=1
    return ans

# h2=sum of Manhattan distance of each tile from the goal position.
def h2(start_state,goal_state):
    ans=0
    for i in range(0,3):
        for j in range(0,3):
            if(start_state[i][j]!='B'):

                for i_temp in range(0,3):
                    for j_temp in range(0,3):
                        if(goal_state[i_temp][j_temp]==start_state[i][j]):
                            x=i_temp
                            y=j_temp
            
                ans+=abs(x-i)+abs(y-j)
    return ans


# Hill climbing Algorithm with h1
def hill_climbing_h1(start_state,goal_state):
    a=[-1,1]
    b=[-1,1]
    test=1
    while(start_state!=goal_state and test<=50):
        print(test)
        print("*************Start************")
        print("heurestic: ",h1(start_state,goal_state))
        
        # B location
        for i in range(0,3):
            for j in range(0,3):
                if(start_state[i][j]=='B'):
                    x=i
                    y=j
            
        heurestic=[]
        for i in a:
            if(0<=x+i and x+i<=2):
                temp_start_state=copy.deepcopy(start_state)
                temp_start_state[x+i][y],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x+i][y]
                heurestic.append([h1(temp_start_state,goal_state),x+i,y])

        for j in b:
            if(0<=y+j and y+j<=2):
                temp_start_state=copy.deepcopy(start_state)
                temp_start_state[x][y+j],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x][y+j]
                heurestic.append([h1(temp_start_state,goal_state),x,y+j])

        min=999
        for i in range(0,len(heurestic)):
            if(heurestic[i][0]<=min):
                min=heurestic[i][0]
                pos=i
        
        start_state[heurestic[pos][1]][heurestic[pos][2]],start_state[x][y]=start_state[x][y],start_state[heurestic[pos][1]][heurestic[pos][2]]
        
        for i in start_state:
            print(i)
        
        test+=1
        print("*************End***************")
        
    if(start_state==goal_state):
        print("\n\nHill Climb Algorithm (h1)")
        print("!!!!!!!Reached Goal State!!!!!!")
        for i in start_state:
            print(i)
        
        print("\nTotal states explored: ",test)
        print("\nTotal States to optimal path: ",test)
        
        #print final state in optimal path
        print("\nOptimal path cost: ",test)

    else:
        print("Failed :<")
        print("**State:**")
        for i in start_state:
            print(i)
        print("Total states explored: ",test)



# Hill climbing Algorithm with h2
def hill_climbing_h2(start_state,goal_state):
    a=[-1,1]
    b=[-1,1]
    test=1
    while(start_state!=goal_state and test<=50):
        print(test)
        print("*************Start************")
        print("heurestic: ",h1(start_state,goal_state))
        
        # B location
        for i in range(0,3):
            for j in range(0,3):
                if(start_state[i][j]=='B'):
                    x=i
                    y=j
            
        heurestic=[]
        for i in a:
            if(0<=x+i and x+i<=2):
                temp_start_state=copy.deepcopy(start_state)
                temp_start_state[x+i][y],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x+i][y]
                heurestic.append([h2(temp_start_state,goal_state),x+i,y])

        for j in b:
            if(0<=y+j and y+j<=2):
                temp_start_state=copy.deepcopy(start_state)
                temp_start_state[x][y+j],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x][y+j]
                heurestic.append([h2(temp_start_state,goal_state),x,y+j])

        min=999
        for i in range(0,len(heurestic)):
            if(heurestic[i][0]<=min):
                min=heurestic[i][0]
                pos=i
        
        start_state[heurestic[pos][1]][heurestic[pos][2]],start_state[x][y]=start_state[x][y],start_state[heurestic[pos][1]][heurestic[pos][2]]
        
        for i in start_state:
            print(i)
        
        test+=1
        print("*************End***************")
        
    if(start_state==goal_state):
        print("\n\nHill Climb Algorithm (h2)")
        print("!!!!!!!Reached Goal State!!!!!!")
        for i in start_state:
            print(i)
        
        print("\nTotal states explored: ",test)
        print("\nTotal States to optimal path: ",test)
        
        #print final state in optimal path
        print("\nOptimal path cost: ",test)

    else:
        print("Failed :<")
        print("**State:**")
        for i in start_state:
            print(i)
        print("Total states explored: ",test)



start_state=[[3,1,2],[4,5,8],[6,'B',7]]
goal_state=[['B',1,2],[3,4,5],[6,7,8]]


print(h1(start_state,goal_state))
print(h2(start_state,goal_state))

print("\n\n\n******* Hill climbing using H1 *******")
hill_climbing_h1(copy.deepcopy(start_state),goal_state)
print("\n\n\n******* Hill climbing using H2 *******")
hill_climbing_h2(copy.deepcopy(start_state),goal_state)




