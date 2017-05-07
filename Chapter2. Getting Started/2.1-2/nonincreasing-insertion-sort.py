
def sort(array):
    for i in range(1, len(array), 1):
        tempValue = array[i];
        j = i-1;
        while j >= 0 and array[j] <  tempValue:
            array[j+1] = array[j];
            j = j - 1;
        array[j+1] = tempValue;

array = [1,2,3,4,5,6];
sort(array)
print(array);


array = [6,5,4,3,2,1];
sort(array)
print(array);

array = [1];
sort(array)
print(array);