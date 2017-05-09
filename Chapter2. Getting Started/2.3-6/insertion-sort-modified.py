
def binary_search(array, l, r, value):
        middle = int((l+r)/2);
        if array[middle] >= value:
            if array[l]<=value:
                return _search(array, l, middle, value);
            else:
                return l;
        else:
            if array[r]>=value:
                return _search(array, middle+1, r, value);
            else:
                return r+1;

def sort(array):
    for i in range(1, len(array), 1):
        tempValue = array[i];
        index = binary_search(array, 0, i-1, tempValue);
        array.insert(index, tempValue);
        array.pop(i+1);
    return array;

print(sort([1,2,3,4,5]));
print(sort([5,4,3,2,1]));
print(sort([1]));
print(sort([]));