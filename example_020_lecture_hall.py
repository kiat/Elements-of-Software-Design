

# Returns the maximum count of non-conflicting activities that can be performed by a single person
def lecture_hall_max_number_DP(activities):

    # Sort the activities according to increasing order of their start time
    activities.sort(key=lambda x: x[1][0])

    # L[i] stores the maximum count of non-conflicting activities ending at i'th activity
    L = [0] * len(activities)

    for i in range(len(activities)):
        # consider each `j` less than `i`
        for j in range(i):
            # L[i] = max(L[j]), where `activities[j].finish` is less than `activities[i].start`
            if activities[j][1][1] < activities[i][1][0] and L[i] < L[j]:
                L[i] = L[j]

        # increment L[i] since it ends at the i'th activities
        L[i] = L[i] + 1

    # return the maximum activities length in the list
    return max(L)



# Find the maximum number of non-conflicting activities that can be performed by a single person
def lecture_hall_DP(activities):
 
    # sort the activities according to increasing order of their start time
    activities.sort(key=lambda x: x[1][0])
 
    # `L[i]` stores the maximum non-conflicting activities that end at i'th activity
    L = [[] for _ in range(len(activities))]
 
    for i in range(len(activities)):
        # consider each `j` less than `i`
        for j in range(i):
            # L[i] = max(L[j]), where `activities[j].finish` is less than `activities[i].start`
            start, finish = (activities[i][1][0], activities[j][1][1])
            if finish < start and len(L[i]) < len(L[j]):
                L[i] = L[j].copy()
 
        # `L[i]` ends at i'th activities
        L[i].append(activities[i])
 
    # find the list having a maximum size
    max = []
    for pair in L:
        if len(max) < len(pair):
            max = pair
 
    # print maximum non-conflicting activities
    print(max)


def lecture_hall_greedy(activities):
    '''Given a class list returns the maximum 
    possible class count to fit in a lecture hall during a day'''

    max = []

    # First we sort the list based on their finish time.
    activities.sort(key=lambda x: x[1][1])
    last_finish = activities[0][1][1]
    max.append(activities[0])

    for i in range(1, len(activities)):
        # Include if the start of the next lecture in the sorted list is after the last selected lecture
        if(activities[i][1][0] >= last_finish):
            max.append(activities[i])
            # then this is our last finish time.
            last_finish = activities[i][1][1]
    print(max)
    return max


def lecture_hall_max_number_greedy(activities):

    '''Given a class list returns the maximum 
    possible class count to fit in a lecture hall during a day'''

    count = 1

    # First we sort the list based on their finish time. 
    activities.sort(key=lambda x: x[1][1])
    last_finish = activities[0][1][1]
   
    for i in range(1, len(activities)):
        # Include if the start of the next lecture in the sorted list is after the last selected lecture 
        if(activities[i][1][0] >= last_finish):
            count +=1
            last_finish = activities[i][1][1] # then this is our last finish time. 
    return count
    

if __name__ == "__main__":

    classes = [
        ('class-1', (1, 4)), ('class-2', (3, 5)), 
        ('class-3', (0, 6)), ('class-4', (5, 7)),
        ('class-6', (5, 9)), ('class-7', (6, 10)), 
        ('class-7', (6, 10)), ('class-8', (8, 11)), 
        ('class-9', (8, 12)), ('class-10', (2, 14)),
        ('class-11', (12, 16)), ('class-12', (1, 5)),
        ('class-13', (2, 4)),  ('class-14', (13, 17))]
    
    # classes2= []
    
    # lecture_hall_DP(classes)
    # print("Max count is: ",  lecture_hall_max_number_DP(classes))


    lecture_hall_greedy(classes)
    print("Max count is: ",  lecture_hall_max_number_greedy(classes))
