
def sort(array):                               #cost    times
    for i in range(0, len(array)-1, 1):        #c1      n
        smallest = array[i];                   #c2      n-1
        smallestIndex = i;                     #c3      n-1
        for j in range(i+1, len(array), 1):    #c4      n*(n+1)/2
            if array[j] < smallest:            #c5      n*(n+1)/2 - 1
                smallest = array[j];           #c6      t
                smallestIndex = j;             #c7      t
        array[smallestIndex] = array[i];       #c8      n-1
        array[i] = smallest;                   #c9      n-1
    return array;

print(sort([1,2,3,4,5]));
print(sort([5,4,3,2,1]));
print(sort([1]));
print(sort([]));