
#################
# Merge Sort
#################

def _merge(A,p,r,q):
    L = A[p:r+1];
    R = A[r+1:q+1];
    index = p;
    while len(R)>0 and len(L)>0:
        if (L[0]<R[0]):
            A[index] = L.pop(0);
        else:
            A[index] = R.pop(0);
        index = index+1;
    for i in range(0, len(L),1):
        A[index] = L.pop(0);
        index = index + 1;
    for i in range(0, len(R), 1):
        A[index] = R.pop(0);
        index = index + 1;

def _sort(array, l, r):
    if r >l:
        _sort(array,l, int((l+r)/2));
        _sort(array, int((l+r)/2+1),r);
        _merge(array, l, int((l+r)/2),r)

def sort(array):
    _sort(array,0, len(array)-1);
    return array;

################
# Binary Search
################
def binarySearch(array, l, r, value):
    if l==r:
        if array[l] == value:
            return l;
    else:
        middle = int((l+r)/2);
        if array[middle] >= value and array[l]<=value:
            return binarySearch(array, l, middle, value);
        if array[middle] < value and array[r]>=value:
            return binarySearch(array, middle+1, r, value);
        return None;

def findIfSumExists(array, value):
    array = sort(array); #Theta(n*lg(n))
    for i in range(0, len(array)-1, 1): #Theta(n)
        nextElementValue = value - array[i];
        if (binarySearch(array, i+1, len(array)-1, nextElementValue)) != None: #Theta(lg(n))
            return True;
    return False;

print(findIfSumExists([1,2,3,4,5], 6));
print(findIfSumExists([1,2,3,4,5], 1));
print(findIfSumExists([5,2,3,4,1], 5));
print(findIfSumExists([5], 5));
print(findIfSumExists([], 5));