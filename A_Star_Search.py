#if u want to run A* search uncomment below example and last output lines and run this file
#start_state=[[1,2,3],['B',4,5],[6,7,8]]
# goal_state=[[2,3,5],[6,1,8],[4,7,'B']]


#to make duplicate list
import copy

#priority queue customized for lists
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item):
        heapq.heappush(self._queue, (item[0], self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __len__(self):
        return len(self._queue)
    
    def items(self):
        return [item[2] for item in self._queue]

#time start
import time





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



# A_Star_Search Algorithm with h1
def A_Star_Search_h1(start_state,goal_state):
    start_time = time.time()
    a=[-1,1]
    b=[-1,1]
    test=1

    # B location
    for i in range(0,3):
        for j in range(0,3):
            if(start_state[i][j]=='B'):
                x=i
                y=j

    level=0
    queue=PriorityQueue()
    # each element in queue is a list 
    # 1st element in list is heurestic
    # 2nd element in list is state
    # 3st element in list is list of optimal path to that current state

    queue.push([h1(start_state,goal_state)+level,start_state,level,[[0]]])

    visited=[]

    flag=True

    while (len(queue)!=0 and test<=100):
        print("\n")
        print(test)

        # print("*************Start************")
        
        #uncomment to print queue at that state
        # print("***Queue:***")
        # for item in queue.items():
        #     print(item[0],item[1],item[2])
        # print("******")
        

        #print location
        l=queue.pop()
        print("**State:**")
        for i in l[1]:
            print(i)
        print("******")

        #B location
        for i in range(0,3):
            for j in range(0,3):
                if(l[1][i][j]=='B'):
                    x=i
                    y=j

        temp_level=l[2]
        print("heurestic: ",l[0])

        if(l[1]==goal_state):
            flag=False 
            print("\n\n\n")
            print("\n\n\n A* Search (h1)")
            print("!!!!!!!Reached Goal State!!!!!!")
            for i in l[1]:
                print(i)
            
            print("\nTotal states explored: ",test)
            print("\nTotal States to optimal path: ",l[2])
            
            print("\nOptimal Path: ")

            num=0
            for i in l[3]:
                if(num!=0):
                    print("State ",num," :")
                    for j in i:
                        print(j) 
                num+=1

            #print final state in optimal path
            print("State ",num," :")
            for i in l[1]:
                print(i)


            print("\nOptimal path cost: ",l[0])
            break


        else:
            #explore neighbors
            for i in a:
                if(0<=x+i and x+i<=2):
                    temp_start_state=copy.deepcopy(l[1])
                    temp_start_state[x+i][y],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x+i][y]
                    
                #make sure visited nodes are not visited again
                    flag=False
                    for i in visited:
                        if i[0]==h1(temp_start_state,goal_state)+temp_level+1 and i[1]==temp_start_state:
                            flag=True
                            break
                #if not visited then push
                    if(flag==False):
                        # temp to make list for optimal path
                        temp=l[3]+[l[1]]
                        queue.push([h1(temp_start_state,goal_state)+temp_level+1,temp_start_state,temp_level+1,temp])
                        visited.append([h1(temp_start_state,goal_state)+temp_level+1,temp_start_state])


            for j in b:
                if(0<=y+j and y+j<=2):
                    temp_start_state=copy.deepcopy(l[1])
                    temp_start_state[x][y+j],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x][y+j]

                #make sure visited nodes are not visited again
                    flag=False
                    for i in visited:
                        if i[0]==h1(temp_start_state,goal_state)+temp_level+1 and i[1]==temp_start_state:
                            flag=True
                            break
                #if not visited then push
                    if(flag==False):
                        temp=l[3]+[l[1]]
                        queue.push([h1(temp_start_state,goal_state)+temp_level+1,temp_start_state,temp_level+1,temp])
                        visited.append([h1(temp_start_state,goal_state)+temp_level+1,temp_start_state])

        test+=1
        print("\n")

    if(test>=50 and flag):
        l=queue.pop()
        print("Failed :<")
        print("**State:**")
        for i in l[1]:
            print(i)
        print("Total states explored: ",test)

        

    #Display time
    end_time = time.time()
    total_time = end_time - start_time
    print("\n\nTime taken:", total_time, "seconds")



# A_Star_Search Algorithm with h2
def A_Star_Search_h2(start_state,goal_state):
    start_time = time.time()
    a=[-1,1]
    b=[-1,1]
    test=1

    # B location
    for i in range(0,3):
        for j in range(0,3):
            if(start_state[i][j]=='B'):
                x=i
                y=j

    level=0
    queue=PriorityQueue()
    # each element in queue is a list 
    # 1st element in list is heurestic
    # 2nd element in list is state
    # 3st element in list is list of optimal path to that current state

    queue.push([h2(start_state,goal_state)+level,start_state,level,[[0]]])

    visited=[]

    flag=True

    while (len(queue)!=0 and test<=100):
        print("\n")
        print(test)

        # print("*************Start************")
        
        #uncomment to print queue at that state
        # print("***Queue:***")
        # for item in queue.items():
        #     print(item[0],item[1],item[2])
        # print("******")
        

        #print location
        l=queue.pop()
        print("**State:**")
        for i in l[1]:
            print(i)
        print("******")

        #B location
        for i in range(0,3):
            for j in range(0,3):
                if(l[1][i][j]=='B'):
                    x=i
                    y=j

        temp_level=l[2]
        print("heurestic: ",l[0])

        if(l[1]==goal_state):
            flag=False 
            print("\n\n\n")
            
            print("\n\n\n A* Search (h2)")
            print("!!!!!!!Reached Goal State!!!!!!")
            for i in l[1]:
                print(i)
            
            print("\nTotal states explored: ",test)
            print("\nTotal States to optimal path: ",l[2])
            
            print("\nOptimal Path: ")

            num=0
            for i in l[3]:
                if(num!=0):
                    print("State ",num," :")
                    for j in i:
                        print(j) 
                num+=1

            #print final state in optimal path
            print("State ",num," :")
            for i in l[1]:
                print(i)


            print("\nOptimal path cost: ",l[0])
            break


        else:
            #explore neighbors
            for i in a:
                if(0<=x+i and x+i<=2):
                    temp_start_state=copy.deepcopy(l[1])
                    temp_start_state[x+i][y],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x+i][y]
                    
                #make sure visited nodes are not visited again
                    flag=False
                    for i in visited:
                        if i[0]==h2(temp_start_state,goal_state)+temp_level+1 and i[1]==temp_start_state:
                            flag=True
                            break
                #if not visited then push
                    if(flag==False):
                        # temp to make list for optimal path
                        temp=l[3]+[l[1]]
                        queue.push([h2(temp_start_state,goal_state)+temp_level+1,temp_start_state,temp_level+1,temp])
                        visited.append([h2(temp_start_state,goal_state)+temp_level+1,temp_start_state])


            for j in b:
                if(0<=y+j and y+j<=2):
                    temp_start_state=copy.deepcopy(l[1])
                    temp_start_state[x][y+j],temp_start_state[x][y]=temp_start_state[x][y],temp_start_state[x][y+j]

                #make sure visited nodes are not visited again
                    flag=False
                    for i in visited:
                        if i[0]==h2(temp_start_state,goal_state)+temp_level+1 and i[1]==temp_start_state:
                            flag=True
                            break
                #if not visited then push
                    if(flag==False):
                        temp=l[3]+[l[1]]
                        queue.push([h2(temp_start_state,goal_state)+temp_level+1,temp_start_state,temp_level+1,temp])
                        visited.append([h2(temp_start_state,goal_state)+temp_level+1,temp_start_state])

        test+=1
        print("\n")

    if(test>=50 and flag):
        l=queue.pop()
        print("Failed :<")
        print("**State:**")
        for i in l[1]:
            print(i)
        print("Total states explored: ",test)

        

    #Display time
    end_time = time.time()
    total_time = end_time - start_time
    print("\n\nTime taken:", total_time, "seconds")






# print("\n\n\n******* A* Search using using H1 *******")
# # A_Star_Search_h1(copy.deepcopy(start_state),goal_state)
# print("\n\n\n******* A* Search using using H2 *******")
# A_Star_Search_h2(copy.deepcopy(start_state),goal_state)




