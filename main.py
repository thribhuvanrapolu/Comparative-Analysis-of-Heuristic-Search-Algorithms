#take input

import A_Star_Search
import best_first_search
import copy




start_state=[]
goal_state=[]
print("Enter Start State")
for i in range(0,3):
    temp=[]
    for j in range(0,3):
        num=input()
        temp.append(num)

    start_state.append(temp)


print("Enter Goal State")

for i in range(0,3):
    temp=[]
    for j in range(0,3):
        num=input()
        temp.append(num)

    goal_state.append(temp)

print("Output saved in output.txt")

import sys
original_stdout = sys.stdout
with open('output.txt', 'w') as f:
    # Redirect stdout to the file
    sys.stdout = f

    # Reset stdout back to its original value

    print("\n\n\n******* Best First Search using using H1 *******")
    best_first_search.best_first_search_h1(copy.deepcopy(start_state),goal_state)
    print("\n\n\n******* Best First Search using using H2 *******")
    best_first_search.best_first_search_h2(copy.deepcopy(start_state),goal_state)

    print("\n\n\n******* A* Search using using H1 *******")
    A_Star_Search.A_Star_Search_h1(copy.deepcopy(start_state),goal_state)
    print("\n\n\n******* A* Search using using H2 *******")
    A_Star_Search.A_Star_Search_h2(copy.deepcopy(start_state),goal_state)

    sys.stdout = original_stdout
