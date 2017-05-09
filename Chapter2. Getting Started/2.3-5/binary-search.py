
def _search(array, l, r, value):
    if l==r:
        if array[l] == value:
            return l;
    else:
        middle = int((l+r)/2);
        if array[middle] >= value and array[l]<=value:
            return _search(array, l, middle, value);
        if array[middle] < value and array[r]>=value:
            return _search(array, middle+1, r, value);
        return None;

def search(array, value):
    if len(array) == 0:
        return  None;
    return _search(array,0, len(array)-1, value);

print(search([1,2,3,4,5], 1));
print(search([1,2,3,4,5], 5));
print(search([1], 1));
print(search([1], 5));
print(search([], 5));