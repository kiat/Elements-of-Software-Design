

def lecture_hall(p):

    '''Given a class list returns the maximum 
    possible class count to fit in a lecture hall during a day'''

    count = 1

    # First we sort the list based on their finish time. 
    p.sort(key=lambda x: x[1][1])
    last_finish = p[0][1][1]
   
    for i in range(1, len(p)):
        # Include if the start of the next lecture in the sorted list is after the last selected lecture 
        if(p[i][1][0] > last_finish):
            count +=1
            last_finish = p[i][1][1] # then this is our last finish time. 
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

 
    print("Maximum possible count is: ", lecture_hall(classes))



