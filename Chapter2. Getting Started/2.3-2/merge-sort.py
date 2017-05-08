
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

print(sort([1,2,3,4,5]));
print(sort([5,4,3,2,1]));
print(sort([5,4,1,2,3]));
print(sort([1]));
print(sort([]));