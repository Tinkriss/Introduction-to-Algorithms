
def _merge(A,p,r,q):
    L = A[p:r+1];
    R = A[r+1:q+1];
    index = p;
    permutation_count = 0;
    while len(R)>0 and len(L)>0:
        if (L[0]<R[0]):
            A[index] = L.pop(0);
        else:
            A[index] = R.pop(0);
            permutation_count = permutation_count  + len(L);
        index = index+1;
    for i in range(0, len(L),1):
        A[index] = L.pop(0);
        index = index + 1;
    for i in range(0, len(R), 1):
        A[index] = R.pop(0);
        index = index + 1;
    return permutation_count;

def _sort(array, l, r):
    permutation_count = 0;
    if r >l:
        permutation_count = permutation_count + _sort(array,l, int((l+r)/2));
        permutation_count = permutation_count + _sort(array, int((l+r)/2+1),r);
        permutation_count = permutation_count + _merge(array, l, int((l+r)/2),r);
    return permutation_count;

def sort(array):
    permutation_count = _sort(array,0, len(array)-1);
    return permutation_count;

print(sort([1,2,3,4,5]));
print(sort([2,1]));
print(sort([5,4,3,2,1]));
print(sort([5,4,1,2,3]));
print(sort([1]));
print(sort([]));